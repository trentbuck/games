#!/usr/bin/python3
import sqlite3
import subprocess
import tempfile
import pathlib

prefix = 'Endless Sky ver. '
version, = [
    line[len(prefix):].strip()
    for line in subprocess.run(
            ['endless-sky', '--version'],
            check=True,
            text=True,
            stderr=subprocess.PIPE).stderr.splitlines()
    if line.startswith(prefix)]
db_path = pathlib.Path(f'endless-sky-{version}.db').resolve()

if False:

    def import_table(table_name, *args):
        with tempfile.TemporaryDirectory() as td_str:
            td = pathlib.Path(td_str)
            csv_path = td / f'{table_name}.csv'
            csv_path.write_bytes(subprocess.check_output(['endless-sky', *args]).replace(b'\n', b'\r\n'))
            subprocess.check_call(
                ['sqlite3', '-csv', '-header', db_path, f".import '{table_name}.csv' {table_name}"],
                cwd=td)

else:

    # Try forcing everything to be an integer column affinity, so
    # sqlite will try to interpret everythign as integers, then reals, then text.
    def import_table(table_name, *args):
        with tempfile.TemporaryDirectory() as td_str:
            td = pathlib.Path(td_str)
            csv_path = td / f'{table_name}.csv'
            csv_str = subprocess.check_output(['endless-sky', *args], text=True).replace('\n', '\r\n')
            csv_path.write_text(csv_str)
            columns_str, _, _ = csv_str.partition('\r\n')
            columns_str = ','.join(
                f'{c} I' if c.startswith('"') else f'"{c}" I'  # yuk
                for c in columns_str.split(','))
            subprocess.check_call(
                ['sqlite3', '-csv', '-header', db_path, f"CREATE TABLE {table_name} ({columns_str})", f".import --skip 1 {table_name}.csv {table_name}"],
                cwd=td)


ratings_schema = '''
-- NOTE: if the ratings table has 5 options, 0 through 4, then you need to multiply the logₘₐₓ(current) by 4, not 5!
-- NOTE: if smaller-is-better (e.g. cost, mass) then we take away the number from 4.
-- NOTE: "outfit space" bigger is better, because it's stored as a negative number.
drop view if exists power★;
create view power★ as
select name
     ,  round((0
        + (4 - 4 * log((select 1 + max("cost") - min("cost") from power), 1 + "cost" - (select min("cost") from power)))
        + (4 - 4 * log((select 1 + max("mass") - min("mass") from power), 1 + "mass" - (select min("mass") from power)))
        + (4 * log((select 1 + max("outfit space") - min("outfit space") from power), 1 + "outfit space" - (select min("outfit space") from power)))
        + (4 * log((select 1 + max("energy generation") - min("energy generation") from power), 1 + "energy generation" - (select min("energy generation") from power)))
        + (4 * log((select 1 + max("heat generation") - min("heat generation") from power), 1 + "heat generation" - (select min("heat generation") from power)))
        + (4 * log((select 1 + max("energy capacity") - min("energy capacity") from power), 1 + "energy capacity" - (select min("energy capacity") from power)))
        ) / 6.0 -- this is how many columns we're averaging
        , 2)
       AS overall
     , cost★.t AS cost
     , mass★.t AS mass
     , "outfit space★".t AS "outfit space"
     , "energy generation★".t AS "energy generation"
     , "heat generation★".t AS "heat generation"
     , "energy capacity★".t AS "energy capacity"
from power
left join ratings cost★ on (cost★.n = round(4 - 4 * log((select 1 + max("cost") - min("cost") from power), 1 + "cost" - (select min("cost") from power)), 0))
left join ratings mass★ on (mass★.n = round(4 - 4 * log((select 1 + max("mass") - min("mass") from power), 1 + "mass" - (select min("mass") from power)), 0))
left join ratings "outfit space★" on ("outfit space★".n = round(4 * log((select 1 + max("outfit space") - min("outfit space") from power), 1 + "outfit space" - (select min("outfit space") from power)), 0))
left join ratings "energy generation★" on ("energy generation★".n = round(4 * log((select 1 + max("energy generation") - min("energy generation") from power), 1 + "energy generation" - (select min("energy generation") from power)), 0))
left join ratings "heat generation★" on ("heat generation★".n = 4 - round(4 * log((select 1 + max("heat generation") - min("heat generation") from power), 1 + "heat generation" - (select min("heat generation") from power)), 0))
left join ratings "energy capacity★" on ("energy capacity★".n = round(4 * log((select 1 + max("energy capacity") - min("energy capacity") from power), 1 + "energy capacity" - (select min("energy capacity") from power)), 0))
ORDER BY overall desc;

drop view if exists reactor★;
create view reactor★ as
-- REACTORS
select
cast(1000*"energy generation"/1.0/-"outfit space"/"heat generation" as int) as "overall efficiency",
cast(100*"energy generation"/1.0/-"outfit space" as int) as "space efficiency",
cast(100*"energy generation"/1.0/"heat generation" as int) as "heat efficiency",
 * from power
 where "energy generation"
--  and "space efficiency" between 15 and 99
--  and "heat efficiency" between 20 and 99
 -- order by 2 desc, 3 desc;
 order by mass desc;

-- BATTERIES
drop view if exists batteries★;
create view batteries★ as
select
cast("energy capacity"/1.0/-"outfit space" as int) as "space efficiency",
 * from power
--  where "energy capacity" and "space efficiency" between 300 and 1100
 order by 1 desc;

-- Ka'Het engines drain energy constantly, rather than only when they're running.
-- This isn't shown in "endless-sky --engines", so manually fudge those columns.
UPDATE engines SET "thrust energy/s" = 654 WHERE "thrust energy/s" = 0 AND name = 'Vareti Engine Block';
UPDATE engines SET "thrust energy/s" = 409 WHERE "thrust energy/s" = 0 AND name = 'Telis Engine Nacelles';
UPDATE engines SET "thrust energy/s" = 301 WHERE "thrust energy/s" = 0 AND name = 'Maeri Engine Nacelles';
UPDATE engines SET "thrust energy/s" = 194 WHERE "thrust energy/s" = 0 AND name = 'Ka''het Sustainer Nacelles';
UPDATE engines SET "thrust energy/s" = 194 WHERE "thrust energy/s" = 0 AND name = 'Ka''het Compact Engine';
drop view if exists engines_grouped;
create view engines_grouped as
select
 -- skipping afterburner in the rating system
 cast(sum("thrust/s" + "turn/s") / - "outfit space" as int) AS "space efficiency",
 cast(sum("thrust/s" + "turn/s") / sum("thrust energy/s" + "turn energy/s") as int) AS "energy efficiency",
 cast(sum("thrust/s" + "turn/s") / sum("thrust heat/s" + "turn heat/s") as int) AS "heat efficiency",
 case
 when name like 'Nami %'              then 'Bunrodea Nami'
 when name like 'Ooki %'              then 'Bunrodea Ooki'
 when name like 'Subarashii %'        then 'Bunrodea Subarashii'
 when name like 'Large %'             then 'Coalition Large'
 when name like 'Small %'             then 'Coalition Small'
 when name like '%Baelie%'            then 'Hai Baelie'
 when name like '%Basrem%'            then 'Hai Basrem'
 when name like '%Benga%'             then 'Hai Benga'
 when name like '%Biroo%'             then 'Hai Biroo'
 when name like '%Bondir%'            then 'Hai Bondir'
 when name like '%Bufaer%'            then 'Hai Bufaer'
 when name like 'A%12_ Atomic%'       then 'Human Atomic 12x'
 when name like 'A25_ Atomic%'        then 'Human Atomic 25x'
 when name like 'A37_ Atomic%'        then 'Human Atomic 37x'
 when name like 'A52_ Atomic%'        then 'Human Atomic 52x'
 when name like 'A86_ Atomic%'        then 'Human Atomic 86x'
 when name like 'X1050 %'             then 'Human Ion 1050'
 when name like 'X1_00 %'             then 'Human Ion 1x00'
 when name like 'X2_00 %'             then 'Human Ion 2x00'
 when name like 'X3_00 %'             then 'Human Ion 3x00'
 when name like 'X4_00 %'             then 'Human Ion 4x00'
 when name like 'X5_00 %'             then 'Human Ion 5x00'
 when name like 'Chipmunk %'          then 'Human Plasma Chipmunk'
 when name like 'Greyhound %'         then 'Human Plasma Greyhound'
 when name like 'Impala %'            then 'Human Plasma Impala'
 when name like 'Orca %'              then 'Human Plasma Orca'
 when name like 'Tyrant %'            then 'Human Plasma Tyrant'
 when name like 'Maeri %'             then 'Ka''het Maeri'
 when name like 'Telis %'             then 'Ka''het Telis'
 when name like 'Vareti %'            then 'Ka''het Vareti'
 when name like 'Arkrof GP%'          then 'Korath Arkrof'
 when name like '% (Asteroid Class)'  then 'Korath Asteroid'
 when name like '% (Comet Class)'     then 'Korath Comet'
 when name like 'Farves GP%'          then 'Korath Farves'
 when name like 'Gaktem GP%'          then 'Korath Gaktem'
 when name like '% (Lunar Class)'     then 'Korath Lunar'
 when name like '% (Meteor Class)'    then 'Korath Meteor'
 when name like 'Nelmeb GP%'          then 'Korath Nelmeb'
 when name like '% (Planetary Class)' then 'Korath Planetary'
 when name like '% (Stellar Class)'   then 'Korath Stellar'
 when name like 'Pug Akfar %'         then 'Pug Akfar'
 when name like 'Pug Cormet %'        then 'Pug Cormet'
 when name like 'Pug Lohmar %'        then 'Pug Lohmar'
 when name like 'Medium Graviton %'   then 'Quarg Medium'
 when name like 'Anvil-Class%'        then 'Remnant Anvil'
 when name like 'Crucible-Class%'     then 'Remnant Crucible'
 when name like 'Forge-Class%'        then 'Remnant Forge'
 when name like 'Smelter-Class%'      then 'Remnant Smelter'
 when name like '%Aqra%'              then 'Successor Aqra'
 when name like '%Chyyra%'            then 'Successor Chyyra'
 when name like '%Niis%'              then 'Successor Niis'
 when name like '%Veusa%'             then 'Successor Veusa'
 when name like 'Type 1 %'            then 'Wanderer 1'
 when name like 'Type 2 %'            then 'Wanderer 2'
 when name like 'Type 3 %'            then 'Wanderer 3'
 when name like 'Type 4 %'            then 'Wanderer 4'
 when name like 'Ka''het Compact %'   then 'Ka''het Compact'
 when name like 'Ka''het Sustainer %' then 'Ka''het Sustainer'

-- Skipping these because ICBF?
-- "Bellows-Class Afterburner",640000,8,-11,-11,0,0,0,0,0,0,0,0,0,675000,360,1080,78
-- Afterburner,70000,10,-10,-10,0,0,0,0,0,0,0,0,0,202500,0,600,6
-- "Caldera Afterburner",390000,37,-37,-37,0,0,0,0,0,0,0,0,0,648000,0,2520,30
-- "Capybara Reverse Thruster",20000,20,-20,0,0,0,0,0,0,0,78300,60,108,0,0,0,0
-- "Chiisana Rift Steering",201000,17,-17,-17,0,0,0,48510,156,60,0,0,0,0,0,0,0
-- "Chiisana Rift Thruster",130000,11,-11,-11,41985,69,39,0,0,0,0,0,0,0,0,0,0
-- "Fission Drive",2650000,71,-71,-38,96120,90.48,171.6,28782,35.1,81.9,0,0,0,0,0,0,0
-- "Fusion Drive",80000000,480,-480,-230,974700,660,1980,224640,273,741,230040,294,798,0,0,0,0
-- "Inductive Extractor",120000,12,-12,-12,-43200,-1800,360,0,0,0,0,0,0,0,0,0,0
-- "Ionic Afterburner",340000,16,-16,-16,0,0,0,0,0,0,0,0,0,169560,306,240,1.8
-- "Korath Ark'parat Steering",36000,12,-12,-12,0,0,0,21600,36,42,0,0,0,0,0,0,0
-- "Korath Ark'torbal Thruster",40000,17,-17,-17,48060,66,60,0,0,0,0,0,0,0,0,0,0
-- "Korath Jak'parat Steering",2740000,67,-67,-67,0,0,0,151200,186,474,0,0,0,0,0,0,0
-- "Korath Jak'torbal Thruster",317000,89,-89,-89,340740,354,858,0,0,0,0,0,0,0,0,0,0
-- "MH Blue-Class Steering",28000,24,-24,-24,0,0,0,29880,60,180,0,0,0,0,0,0,0
-- "MH Blue-Class Thruster",32000,27,-27,-27,86400,120,150,0,0,0,0,0,0,0,0,0,0
-- "MH Green-Class Steering",35000,28,-28,-28,0,0,0,37080,66,186,0,0,0,0,0,0,0
-- "MH Green-Class Thruster",44000,32,-32,-32,108000,132,168,0,0,0,0,0,0,0,0,0,0
-- "MH Red-Class Steering",49000,41,-41,-41,0,0,0,68040,150,720,0,0,0,0,0,0,0
-- "MH Red-Class Thruster",50000,41,-41,-41,172800,300,600,0,0,0,0,0,0,0,0,0,0
-- "Magnetoplasma Drive",27000,12,-12,-12,32400,36,18,16200,36,18,32400,36,18,0,0,0,0
-- "R-180 RCS Thrusters",54000,18,-18,-18,0,0,0,45000,90,-180,32400,90,-180,0,0,0,0
-- "R-360 RCS Thrusters",126000,36,-36,-36,0,0,0,102600,180,-360,64800,180,-360,0,0,0,0
-- "R-720 RCS Thrusters",270000,72,-72,-72,0,0,0,221400,360,-540,129600,360,-540,0,0,0,0
-- "RG15 Torch Steering",15000,25,-25,-25,0,0,0,25830,24,51,0,0,0,0,0,0,0
-- "RG15 Torch Thruster",17000,31,-31,-31,62478,42,90,0,0,0,0,0,0,0,0,0,0
-- "RG18 Torch Steering",32000,39,-39,-39,0,0,0,47070,39,90,0,0,0,0,0,0,0
-- "RG18 Torch Thruster",38000,51,-51,-51,110160,75,174,0,0,0,0,0,0,0,0,0,0
-- "RG3 Torch Steering",70000,64,-64,-64,0,0,0,90360,69,168,0,0,0,0,0,0,0
-- "RG3 Torch Thruster",84000,83,-83,-83,194400,132,324,0,0,0,0,0,0,0,0,0,0
-- "Remass Injector",90000,6,-6,-3,0,0,0,0,0,0,0,0,0,324000,180,-1080,14.4
-- "Reverse Thruster",140000,22,-22,0,0,0,0,0,0,0,101016,108,210,0,0,0,0
-- "SC-1 Plasma Engines",21200,21,-21,-21,35370,24,60,14400,21,48,0,0,0,0,0,0,0
-- "SC-12 Plasma Steering",17000,19,-19,-19,0,0,0,26730,27,69,0,0,0,0,0,0,0
-- "SC-12 Plasma Thruster",20900,25,-25,-25,73116,51,135,0,0,0,0,0,0,0,0,0,0
-- "SC-14 Plasma Steering",41500,34,-34,-34,0,0,0,57420,60,177,0,0,0,0,0,0,0
-- "SC-14 Plasma Thruster",52500,45,-45,-45,142560,102,297,0,0,0,0,0,0,0,0,0,0
-- "SC-15 Plasma Thrusters",170400,112,-112,-112,262440,186,570,0,0,0,81900,87,267,0,0,0,0
-- "Volcano Afterburner",70000,10,-10,-10,0,0,0,0,0,0,0,0,0,146340,0,600,7.5
-- `Z-333 "Spark" Fusion Torch`,1800000,333,-33,-33,324000,540,2700,0,0,0,0,0,0,0,0,0,0
-- `Z-3600 "Beam" Amat Torch`,300000000,3600,-360,-360,2.16e+06,900,5400,360000,540,3240,0,0,0,0,0,0,0
-- `Z-666 "Zap" Fusion Torch`,3900000,666,-66,-66,756000,1080,5400,0,0,0,0,0,0,0,0,0,0
-- `Z-999 "Arc" Fusion Torch`,6000000,999,-99,-99,1.296e+06,1620,8100,0,0,0,0,0,0,0,0,0,0


 else 'FIXME'
 end AS clade,
 count(*) as parts,
 sum(cost) as cost,
 sum(mass) as mass,
 sum("outfit space") as "outfit space",
 sum("engine capacity") as "engine capacity",
 sum("thrust/s") as "thrust/s",
 sum("thrust energy/s") as "thrust energy/s",
 sum("thrust heat/s") as "thrust heat/s",
 sum("turn/s") as "turn/s",
 sum("turn energy/s") as "turn energy/s",
 sum("turn heat/s") as "turn heat/s",
 sum("reverse thrust/s") as "reverse thrust/s",
 sum("reverse energy/s") as "reverse energy/s",
 sum("reverse heat/s") as "reverse heat/s",
 sum("afterburner thrust/s") as "afterburner thrust/s",
 sum("afterburner energy/s") as "afterburner energy/s",
 sum("afterburner heat/s") as "afterburner heat/s",
 sum("afterburner fuel/s") as "afterburner fuel/s"
 from engines
 group by clade
 order by
 ("space efficiency" + "energy efficiency" + "heat efficiency")/3.0 desc
 -- "outfit space"
 -- substr(clade, 0, instr(clade, ' ')), mass desc
 -- mass desc
 -- "space efficiency"/10 + "energy efficiency" + "heat efficiency" desc
;



drop view if exists engines_thrusters★;
create view engines_thrusters★ as
-- Use a CTE to hide an insane, unique, near-unobtainable item that is screwing all the stats
WITH engines_ AS (SELECT * FROM engines WHERE name NOT IN ("Fusion Drive", '`Z-3600 "Beam" Amat Torch`') AND "thrust/s" > 0)
select name
     ,  round((0
               + (4 - 4 * log((select 1 + max("cost") - min("cost") from engines_), 1 + "cost" - (select min("cost") from engines_)))
               + (4 - 4 * log((select 1 + max("mass") - min("mass") from engines_), 1 + "mass" - (select min("mass") from engines_)))
               + (4 * log((select 1 + max("outfit space") - min("outfit space") from engines_), 1 + "outfit space" - (select min("outfit space") from engines_)))
               + (4 * log((select 1 + max("engine capacity") - min("engine capacity") from engines_), 1 + "engine capacity" - (select min("engine capacity") from engines_)))
               + (4 * log((select 1 + max("thrust/s") - min("thrust/s") from engines_), 1 + "thrust/s" - (select min("thrust/s") from engines_)))
               + (4 - 4 * log((select 1 + max("thrust energy/s") - min("thrust energy/s") from engines_), 1 + "thrust energy/s" - (select min("thrust energy/s") from engines_)))
               + (4 - 4 * log((select 1 + max("thrust heat/s") - min("thrust heat/s") from engines_), 1 + "thrust heat/s" - (select min("thrust heat/s") from engines_)))
--               + (4 * log((select 1 + max("turn/s") - min("turn/s") from engines_), 1 + "turn/s" - (select min("turn/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("turn energy/s") - min("turn energy/s") from engines_), 1 + "turn energy/s" - (select min("turn energy/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("turn heat/s") - min("turn heat/s") from engines_), 1 + "turn heat/s" - (select min("turn heat/s") from engines_)))
--               + (4 * log((select 1 + max("reverse thrust/s") - min("reverse thrust/s") from engines_), 1 + "reverse thrust/s" - (select min("reverse thrust/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("reverse energy/s") - min("reverse energy/s") from engines_), 1 + "reverse energy/s" - (select min("reverse energy/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("reverse heat/s") - min("reverse heat/s") from engines_), 1 + "reverse heat/s" - (select min("reverse heat/s") from engines_)))
--               + (4 * log((select 1 + max("afterburner thrust/s") - min("afterburner thrust/s") from engines_), 1 + "afterburner thrust/s" - (select min("afterburner thrust/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("afterburner energy/s") - min("afterburner energy/s") from engines_), 1 + "afterburner energy/s" - (select min("afterburner energy/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("afterburner heat/s") - min("afterburner heat/s") from engines_), 1 + "afterburner heat/s" - (select min("afterburner heat/s") from engines_)))
--               + (4 - 4 * log((select 1 + max("afterburner fuel/s") - min("afterburner fuel/s") from engines_), 1 + "afterburner fuel/s" - (select min("afterburner fuel/s") from engines_)))
        ) / 17.0 -- this is how many columns we're averaging
        , 2)
       AS overall
     , "cost★".t as "cost"
     , "mass★".t as "mass"
     , "outfit space★".t as "outfit space"
     , "engine capacity★".t as "engine capacity"
     , "thrust/s★".t as "thrust/s"
     , "thrust energy/s★".t as "thrust energy/s"
     , "thrust heat/s★".t as "thrust heat/s"
     , "turn/s★".t as "turn/s"
     , "turn energy/s★".t as "turn energy/s"
     , "turn heat/s★".t as "turn heat/s"
     , "reverse thrust/s★".t as "reverse thrust/s"
     , "reverse energy/s★".t as "reverse energy/s"
     , "reverse heat/s★".t as "reverse heat/s"
     , "afterburner thrust/s★".t as "afterburner thrust/s"
     , "afterburner energy/s★".t as "afterburner energy/s"
     , "afterburner heat/s★".t as "afterburner heat/s"
     , "afterburner fuel/s★".t as "afterburner fuel/s"
from engines_
left join ratings "cost★" on ("cost★".n = round(4 - 4 * log((select 1 + max("cost") - min("cost") from engines_), 1 + "cost" - (select min("cost") from engines_)), 0))
left join ratings "mass★" on ("mass★".n = round(4 - 4 * log((select 1 + max("mass") - min("mass") from engines_), 1 + "mass" - (select min("mass") from engines_)), 0))
left join ratings "outfit space★" on ("outfit space★".n = round(4 * log((select 1 + max("outfit space") - min("outfit space") from engines_), 1 + "outfit space" - (select min("outfit space") from engines_)), 0))
left join ratings "engine capacity★" on ("engine capacity★".n = round(4 * log((select 1 + max("engine capacity") - min("engine capacity") from engines_), 1 + "engine capacity" - (select min("engine capacity") from engines_)), 0))
left join ratings "thrust/s★" on ("thrust/s★".n = round(4 * log((select 1 + max("thrust/s") - min("thrust/s") from engines_), 1 + "thrust/s" - (select min("thrust/s") from engines_)), 0))
left join ratings "thrust energy/s★" on ("thrust energy/s★".n = round(4 - 4 * log((select 1 + max("thrust energy/s") - min("thrust energy/s") from engines_), 1 + "thrust energy/s" - (select min("thrust energy/s") from engines_)), 0))
left join ratings "thrust heat/s★" on ("thrust heat/s★".n = round(4 - 4 * log((select 1 + max("thrust heat/s") - min("thrust heat/s") from engines_), 1 + "thrust heat/s" - (select min("thrust heat/s") from engines_)), 0))
left join ratings "turn/s★" on ("turn/s★".n = round(4 * log((select 1 + max("turn/s") - min("turn/s") from engines_), 1 + "turn/s" - (select min("turn/s") from engines_)), 0))
left join ratings "turn energy/s★" on ("turn energy/s★".n = round(4 - 4 * log((select 1 + max("turn energy/s") - min("turn energy/s") from engines_), 1 + "turn energy/s" - (select min("turn energy/s") from engines_)), 0))
left join ratings "turn heat/s★" on ("turn heat/s★".n = round(4 - 4 * log((select 1 + max("turn heat/s") - min("turn heat/s") from engines_), 1 + "turn heat/s" - (select min("turn heat/s") from engines_)), 0))
left join ratings "reverse thrust/s★" on ("reverse thrust/s★".n = round(4 * log((select 1 + max("reverse thrust/s") - min("reverse thrust/s") from engines_), 1 + "reverse thrust/s" - (select min("reverse thrust/s") from engines_)), 0))
left join ratings "reverse energy/s★" on ("reverse energy/s★".n = round(4 - 4 * log((select 1 + max("reverse energy/s") - min("reverse energy/s") from engines_), 1 + "reverse energy/s" - (select min("reverse energy/s") from engines_)), 0))
left join ratings "reverse heat/s★" on ("reverse heat/s★".n = round(4 - 4 * log((select 1 + max("reverse heat/s") - min("reverse heat/s") from engines_), 1 + "reverse heat/s" - (select min("reverse heat/s") from engines_)), 0))
left join ratings "afterburner thrust/s★" on ("afterburner thrust/s★".n = round(4 * log((select 1 + max("afterburner thrust/s") - min("afterburner thrust/s") from engines_), 1 + "afterburner thrust/s" - (select min("afterburner thrust/s") from engines_)), 0))
left join ratings "afterburner energy/s★" on ("afterburner energy/s★".n = round(4 - 4 * log((select 1 + max("afterburner energy/s") - min("afterburner energy/s") from engines_), 1 + "afterburner energy/s" - (select min("afterburner energy/s") from engines_)), 0))
left join ratings "afterburner heat/s★" on ("afterburner heat/s★".n = round(4 - 4 * log((select 1 + max("afterburner heat/s") - min("afterburner heat/s") from engines_), 1 + "afterburner heat/s" - (select min("afterburner heat/s") from engines_)), 0))
left join ratings "afterburner fuel/s★" on ("afterburner fuel/s★".n = round(4 - 4 * log((select 1 + max("afterburner fuel/s") - min("afterburner fuel/s") from engines_), 1 + "afterburner fuel/s" - (select min("afterburner fuel/s") from engines_)), 0))
ORDER BY overall desc
;

drop view if exists engines★;
create view engines★ as
-- Use a CTE to hide an insane, unique, near-unobtainable item that is screwing all the stats
WITH engines_ AS (SELECT * FROM engines WHERE name NOT IN ("Fusion Drive"))
select name
     ,  round((0
               + (4 - 4 * log((select 1 + max("cost") - min("cost") from engines_), 1 + "cost" - (select min("cost") from engines_)))
               + (4 - 4 * log((select 1 + max("mass") - min("mass") from engines_), 1 + "mass" - (select min("mass") from engines_)))
               + (4 * log((select 1 + max("outfit space") - min("outfit space") from engines_), 1 + "outfit space" - (select min("outfit space") from engines_)))
               + (4 * log((select 1 + max("engine capacity") - min("engine capacity") from engines_), 1 + "engine capacity" - (select min("engine capacity") from engines_)))
               + (4 * log((select 1 + max("thrust/s") - min("thrust/s") from engines_), 1 + "thrust/s" - (select min("thrust/s") from engines_)))
               + (4 - 4 * log((select 1 + max("thrust energy/s") - min("thrust energy/s") from engines_), 1 + "thrust energy/s" - (select min("thrust energy/s") from engines_)))
               + (4 - 4 * log((select 1 + max("thrust heat/s") - min("thrust heat/s") from engines_), 1 + "thrust heat/s" - (select min("thrust heat/s") from engines_)))
               + (4 * log((select 1 + max("turn/s") - min("turn/s") from engines_), 1 + "turn/s" - (select min("turn/s") from engines_)))
               + (4 - 4 * log((select 1 + max("turn energy/s") - min("turn energy/s") from engines_), 1 + "turn energy/s" - (select min("turn energy/s") from engines_)))
               + (4 - 4 * log((select 1 + max("turn heat/s") - min("turn heat/s") from engines_), 1 + "turn heat/s" - (select min("turn heat/s") from engines_)))
               + (4 * log((select 1 + max("reverse thrust/s") - min("reverse thrust/s") from engines_), 1 + "reverse thrust/s" - (select min("reverse thrust/s") from engines_)))
               + (4 - 4 * log((select 1 + max("reverse energy/s") - min("reverse energy/s") from engines_), 1 + "reverse energy/s" - (select min("reverse energy/s") from engines_)))
               + (4 - 4 * log((select 1 + max("reverse heat/s") - min("reverse heat/s") from engines_), 1 + "reverse heat/s" - (select min("reverse heat/s") from engines_)))
               + (4 * log((select 1 + max("afterburner thrust/s") - min("afterburner thrust/s") from engines_), 1 + "afterburner thrust/s" - (select min("afterburner thrust/s") from engines_)))
               + (4 - 4 * log((select 1 + max("afterburner energy/s") - min("afterburner energy/s") from engines_), 1 + "afterburner energy/s" - (select min("afterburner energy/s") from engines_)))
               + (4 - 4 * log((select 1 + max("afterburner heat/s") - min("afterburner heat/s") from engines_), 1 + "afterburner heat/s" - (select min("afterburner heat/s") from engines_)))
               + (4 - 4 * log((select 1 + max("afterburner fuel/s") - min("afterburner fuel/s") from engines_), 1 + "afterburner fuel/s" - (select min("afterburner fuel/s") from engines_)))
        ) / 17.0 -- this is how many columns we're averaging
        , 2)
       AS overall
     , "cost★".t as "cost"
     , "mass★".t as "mass"
     , "outfit space★".t as "outfit space"
     , "engine capacity★".t as "engine capacity"
     , "thrust/s★".t as "thrust/s"
     , "thrust energy/s★".t as "thrust energy/s"
     , "thrust heat/s★".t as "thrust heat/s"
     , "turn/s★".t as "turn/s"
     , "turn energy/s★".t as "turn energy/s"
     , "turn heat/s★".t as "turn heat/s"
     , "reverse thrust/s★".t as "reverse thrust/s"
     , "reverse energy/s★".t as "reverse energy/s"
     , "reverse heat/s★".t as "reverse heat/s"
     , "afterburner thrust/s★".t as "afterburner thrust/s"
     , "afterburner energy/s★".t as "afterburner energy/s"
     , "afterburner heat/s★".t as "afterburner heat/s"
     , "afterburner fuel/s★".t as "afterburner fuel/s"
from engines_
left join ratings "cost★" on ("cost★".n = round(4 - 4 * log((select 1 + max("cost") - min("cost") from engines_), 1 + "cost" - (select min("cost") from engines_)), 0))
left join ratings "mass★" on ("mass★".n = round(4 - 4 * log((select 1 + max("mass") - min("mass") from engines_), 1 + "mass" - (select min("mass") from engines_)), 0))
left join ratings "outfit space★" on ("outfit space★".n = round(4 * log((select 1 + max("outfit space") - min("outfit space") from engines_), 1 + "outfit space" - (select min("outfit space") from engines_)), 0))
left join ratings "engine capacity★" on ("engine capacity★".n = round(4 * log((select 1 + max("engine capacity") - min("engine capacity") from engines_), 1 + "engine capacity" - (select min("engine capacity") from engines_)), 0))
left join ratings "thrust/s★" on ("thrust/s★".n = round(4 * log((select 1 + max("thrust/s") - min("thrust/s") from engines_), 1 + "thrust/s" - (select min("thrust/s") from engines_)), 0))
left join ratings "thrust energy/s★" on ("thrust energy/s★".n = round(4 - 4 * log((select 1 + max("thrust energy/s") - min("thrust energy/s") from engines_), 1 + "thrust energy/s" - (select min("thrust energy/s") from engines_)), 0))
left join ratings "thrust heat/s★" on ("thrust heat/s★".n = round(4 - 4 * log((select 1 + max("thrust heat/s") - min("thrust heat/s") from engines_), 1 + "thrust heat/s" - (select min("thrust heat/s") from engines_)), 0))
left join ratings "turn/s★" on ("turn/s★".n = round(4 * log((select 1 + max("turn/s") - min("turn/s") from engines_), 1 + "turn/s" - (select min("turn/s") from engines_)), 0))
left join ratings "turn energy/s★" on ("turn energy/s★".n = round(4 - 4 * log((select 1 + max("turn energy/s") - min("turn energy/s") from engines_), 1 + "turn energy/s" - (select min("turn energy/s") from engines_)), 0))
left join ratings "turn heat/s★" on ("turn heat/s★".n = round(4 - 4 * log((select 1 + max("turn heat/s") - min("turn heat/s") from engines_), 1 + "turn heat/s" - (select min("turn heat/s") from engines_)), 0))
left join ratings "reverse thrust/s★" on ("reverse thrust/s★".n = round(4 * log((select 1 + max("reverse thrust/s") - min("reverse thrust/s") from engines_), 1 + "reverse thrust/s" - (select min("reverse thrust/s") from engines_)), 0))
left join ratings "reverse energy/s★" on ("reverse energy/s★".n = round(4 - 4 * log((select 1 + max("reverse energy/s") - min("reverse energy/s") from engines_), 1 + "reverse energy/s" - (select min("reverse energy/s") from engines_)), 0))
left join ratings "reverse heat/s★" on ("reverse heat/s★".n = round(4 - 4 * log((select 1 + max("reverse heat/s") - min("reverse heat/s") from engines_), 1 + "reverse heat/s" - (select min("reverse heat/s") from engines_)), 0))
left join ratings "afterburner thrust/s★" on ("afterburner thrust/s★".n = round(4 * log((select 1 + max("afterburner thrust/s") - min("afterburner thrust/s") from engines_), 1 + "afterburner thrust/s" - (select min("afterburner thrust/s") from engines_)), 0))
left join ratings "afterburner energy/s★" on ("afterburner energy/s★".n = round(4 - 4 * log((select 1 + max("afterburner energy/s") - min("afterburner energy/s") from engines_), 1 + "afterburner energy/s" - (select min("afterburner energy/s") from engines_)), 0))
left join ratings "afterburner heat/s★" on ("afterburner heat/s★".n = round(4 - 4 * log((select 1 + max("afterburner heat/s") - min("afterburner heat/s") from engines_), 1 + "afterburner heat/s" - (select min("afterburner heat/s") from engines_)), 0))
left join ratings "afterburner fuel/s★" on ("afterburner fuel/s★".n = round(4 - 4 * log((select 1 + max("afterburner fuel/s") - min("afterburner fuel/s") from engines_), 1 + "afterburner fuel/s" - (select min("afterburner fuel/s") from engines_)), 0))
ORDER BY overall desc
;

drop view if exists weapons★;
create view weapons★ as
WITH weapons_ AS (SELECT * FROM weapons WHERE cost > 0)
select name
     , category
     ,  round((0
               + (4 - 4 * log((select 1 + max("cost") - min("cost") from weapons_), 1 + "cost" - (select min("cost") from weapons_)))
               + (4 - 4 * log((select 1 + max("space") - min("space") from weapons_), 1 + "space" - (select min("space") from weapons_)))
               + (    4 * log((select 1 + max("range") - min("range") from weapons_), 1 + "range" - (select min("range") from weapons_)))
               + (4 - 4 * log((select 1 + max("reload") - min("reload") from weapons_), 1 + "reload" - (select min("reload") from weapons_)))
               + (    4 * log((select 1 + max("burst count") - min("burst count") from weapons_), 1 + "burst count" - (select min("burst count") from weapons_)))
               + (4 - 4 * log((select 1 + max("burst reload") - min("burst reload") from weapons_), 1 + "burst reload" - (select min("burst reload") from weapons_)))
               + (    4 * log((select 1 + max("lifetime") - min("lifetime") from weapons_), 1 + "lifetime" - (select min("lifetime") from weapons_)))
               + (    4 * log((select 1 + max("shots/second") - min("shots/second") from weapons_), 1 + "shots/second" - (select min("shots/second") from weapons_)))
               + (4 - 4 * log((select 1 + max("energy/shot") - min("energy/shot") from weapons_), 1 + "energy/shot" - (select min("energy/shot") from weapons_)))
               + (4 - 4 * log((select 1 + max("heat/shot") - min("heat/shot") from weapons_), 1 + "heat/shot" - (select min("heat/shot") from weapons_)))
               + (4 - 4 * log((select 1 + max("recoil/shot") - min("recoil/shot") from weapons_), 1 + "recoil/shot" - (select min("recoil/shot") from weapons_)))
               + (4 - 4 * log((select 1 + max("energy/s") - min("energy/s") from weapons_), 1 + "energy/s" - (select min("energy/s") from weapons_)))
               + (4 - 4 * log((select 1 + max("heat/s") - min("heat/s") from weapons_), 1 + "heat/s" - (select min("heat/s") from weapons_)))
               + (4 - 4 * log((select 1 + max("recoil/s") - min("recoil/s") from weapons_), 1 + "recoil/s" - (select min("recoil/s") from weapons_)))
               + (    4 * log((select 1 + max("shield/s") - min("shield/s") from weapons_), 1 + "shield/s" - (select min("shield/s") from weapons_)))
               + (    4 * log((select 1 + max("discharge/s") - min("discharge/s") from weapons_), 1 + "discharge/s" - (select min("discharge/s") from weapons_)))
               + (    4 * log((select 1 + max("hull/s") - min("hull/s") from weapons_), 1 + "hull/s" - (select min("hull/s") from weapons_)))
               + (    4 * log((select 1 + max("corrosion/s") - min("corrosion/s") from weapons_), 1 + "corrosion/s" - (select min("corrosion/s") from weapons_)))
               + (    4 * log((select 1 + max("heat dmg/s") - min("heat dmg/s") from weapons_), 1 + "heat dmg/s" - (select min("heat dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("burn dmg/s") - min("burn dmg/s") from weapons_), 1 + "burn dmg/s" - (select min("burn dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("energy dmg/s") - min("energy dmg/s") from weapons_), 1 + "energy dmg/s" - (select min("energy dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("ion dmg/s") - min("ion dmg/s") from weapons_), 1 + "ion dmg/s" - (select min("ion dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("scrambling dmg/s") - min("scrambling dmg/s") from weapons_), 1 + "scrambling dmg/s" - (select min("scrambling dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("slow dmg/s") - min("slow dmg/s") from weapons_), 1 + "slow dmg/s" - (select min("slow dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("disruption dmg/s") - min("disruption dmg/s") from weapons_), 1 + "disruption dmg/s" - (select min("disruption dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("piercing") - min("piercing") from weapons_), 1 + "piercing" - (select min("piercing") from weapons_)))
               + (    4 * log((select 1 + max("fuel dmg/s") - min("fuel dmg/s") from weapons_), 1 + "fuel dmg/s" - (select min("fuel dmg/s") from weapons_)))
--             + (    4 * log((select 1 + max("leak dmg/s") - min("leak dmg/s") from weapons_), 1 + "leak dmg/s" - (select min("leak dmg/s") from weapons_)))
               + (    4 * log((select 1 + max("push/s") - min("push/s") from weapons_), 1 + "push/s" - (select min("push/s") from weapons_)))
               + (    4 * log((select 1 + max("homing") - min("homing") from weapons_), 1 + "homing" - (select min("homing") from weapons_)))
               + (    4 * log((select 1 + max("strength") - min("strength") from weapons_), 1 + "strength" - (select min("strength") from weapons_)))
               + (    4 * log((select 1 + max("deterrence") - min("deterrence") from weapons_), 1 + "deterrence" - (select min("deterrence") from weapons_)))
        ) / 31.0 -- this is how many columns we're averaging
        , 2)
       AS overall
     , "cost★".t as "cost"
     , "cost★".t as "cost"
     , "space★".t as "space"
     , "range★".t as "range"
     , "reload★".t as "reload"
     , "burst count★".t as "burst count"
     , "burst reload★".t as "burst reload"
     , "lifetime★".t as "lifetime"
     , "shots/second★".t as "shots/second"
     , "energy/shot★".t as "energy/shot"
     , "heat/shot★".t as "heat/shot"
     , "recoil/shot★".t as "recoil/shot"
     , "energy/s★".t as "energy/s"
     , "heat/s★".t as "heat/s"
     , "recoil/s★".t as "recoil/s"
     , "shield/s★".t as "shield/s"
     , "discharge/s★".t as "discharge/s"
     , "hull/s★".t as "hull/s"
     , "corrosion/s★".t as "corrosion/s"
     , "heat dmg/s★".t as "heat dmg/s"
     , "burn dmg/s★".t as "burn dmg/s"
     , "energy dmg/s★".t as "energy dmg/s"
     , "ion dmg/s★".t as "ion dmg/s"
     , "scrambling dmg/s★".t as "scrambling dmg/s"
     , "slow dmg/s★".t as "slow dmg/s"
     , "disruption dmg/s★".t as "disruption dmg/s"
     , "piercing★".t as "piercing"
     , "fuel dmg/s★".t as "fuel dmg/s"
     , "leak dmg/s★".t as "leak dmg/s"
     , "push/s★".t as "push/s"
     , "homing★".t as "homing"
     , "strength★".t as "strength"
     , "deterrence★".t as "deterrence"
from weapons_
left join ratings "cost★" on ("cost★".n =                         round(4 - 4 * log((select 1 + max("cost") - min("cost") from weapons_), 1 + "cost" - (select min("cost") from weapons_)), 0))
left join ratings "space★" on ("space★".n =                       round(4 - 4 * log((select 1 + max("space") - min("space") from weapons_), 1 + "space" - (select min("space") from weapons_)), 0))
left join ratings "range★" on ("range★".n =                       round(    4 * log((select 1 + max("range") - min("range") from weapons_), 1 + "range" - (select min("range") from weapons_)), 0))
left join ratings "reload★" on ("reload★".n =                     round(4 - 4 * log((select 1 + max("reload") - min("reload") from weapons_), 1 + "reload" - (select min("reload") from weapons_)), 0))
left join ratings "burst count★" on ("burst count★".n =           round(    4 * log((select 1 + max("burst count") - min("burst count") from weapons_), 1 + "burst count" - (select min("burst count") from weapons_)), 0))
left join ratings "burst reload★" on ("burst reload★".n =         round(4 - 4 * log((select 1 + max("burst reload") - min("burst reload") from weapons_), 1 + "burst reload" - (select min("burst reload") from weapons_)), 0))
-- FIXME: lifetime = 1 is a special case for beam weapons...
left join ratings "lifetime★" on ("lifetime★".n =                 round(    4 * log((select 1 + max("lifetime") - min("lifetime") from weapons_), 1 + "lifetime" - (select min("lifetime") from weapons_)), 0))
left join ratings "shots/second★" on ("shots/second★".n =         round(    4 * log((select 1 + max("shots/second") - min("shots/second") from weapons_), 1 + "shots/second" - (select min("shots/second") from weapons_)), 0))
left join ratings "energy/shot★" on ("energy/shot★".n =           round(4 - 4 * log((select 1 + max("energy/shot") - min("energy/shot") from weapons_), 1 + "energy/shot" - (select min("energy/shot") from weapons_)), 0))
left join ratings "heat/shot★" on ("heat/shot★".n =               round(4 - 4 * log((select 1 + max("heat/shot") - min("heat/shot") from weapons_), 1 + "heat/shot" - (select min("heat/shot") from weapons_)), 0))
left join ratings "recoil/shot★" on ("recoil/shot★".n =           round(4 - 4 * log((select 1 + max("recoil/shot") - min("recoil/shot") from weapons_), 1 + "recoil/shot" - (select min("recoil/shot") from weapons_)), 0))
left join ratings "energy/s★" on ("energy/s★".n =                 round(4 - 4 * log((select 1 + max("energy/s") - min("energy/s") from weapons_), 1 + "energy/s" - (select min("energy/s") from weapons_)), 0))
left join ratings "heat/s★" on ("heat/s★".n =                     round(4 - 4 * log((select 1 + max("heat/s") - min("heat/s") from weapons_), 1 + "heat/s" - (select min("heat/s") from weapons_)), 0))
left join ratings "recoil/s★" on ("recoil/s★".n =                 round(4 - 4 * log((select 1 + max("recoil/s") - min("recoil/s") from weapons_), 1 + "recoil/s" - (select min("recoil/s") from weapons_)), 0))
left join ratings "shield/s★" on ("shield/s★".n =                 round(    4 * log((select 1 + max("shield/s") - min("shield/s") from weapons_), 1 + "shield/s" - (select min("shield/s") from weapons_)), 0))
left join ratings "discharge/s★" on ("discharge/s★".n =           round(    4 * log((select 1 + max("discharge/s") - min("discharge/s") from weapons_), 1 + "discharge/s" - (select min("discharge/s") from weapons_)), 0))
left join ratings "hull/s★" on ("hull/s★".n =                     round(    4 * log((select 1 + max("hull/s") - min("hull/s") from weapons_), 1 + "hull/s" - (select min("hull/s") from weapons_)), 0))
left join ratings "corrosion/s★" on ("corrosion/s★".n =           round(    4 * log((select 1 + max("corrosion/s") - min("corrosion/s") from weapons_), 1 + "corrosion/s" - (select min("corrosion/s") from weapons_)), 0))
left join ratings "heat dmg/s★" on ("heat dmg/s★".n =             round(    4 * log((select 1 + max("heat dmg/s") - min("heat dmg/s") from weapons_), 1 + "heat dmg/s" - (select min("heat dmg/s") from weapons_)), 0))
left join ratings "burn dmg/s★" on ("burn dmg/s★".n =             round(    4 * log((select 1 + max("burn dmg/s") - min("burn dmg/s") from weapons_), 1 + "burn dmg/s" - (select min("burn dmg/s") from weapons_)), 0))
left join ratings "energy dmg/s★" on ("energy dmg/s★".n =         round(    4 * log((select 1 + max("energy dmg/s") - min("energy dmg/s") from weapons_), 1 + "energy dmg/s" - (select min("energy dmg/s") from weapons_)), 0))
left join ratings "ion dmg/s★" on ("ion dmg/s★".n =               round(    4 * log((select 1 + max("ion dmg/s") - min("ion dmg/s") from weapons_), 1 + "ion dmg/s" - (select min("ion dmg/s") from weapons_)), 0))
left join ratings "scrambling dmg/s★" on ("scrambling dmg/s★".n = round(    4 * log((select 1 + max("scrambling dmg/s") - min("scrambling dmg/s") from weapons_), 1 + "scrambling dmg/s" - (select min("scrambling dmg/s") from weapons_)), 0))
left join ratings "slow dmg/s★" on ("slow dmg/s★".n =             round(    4 * log((select 1 + max("slow dmg/s") - min("slow dmg/s") from weapons_), 1 + "slow dmg/s" - (select min("slow dmg/s") from weapons_)), 0))
left join ratings "disruption dmg/s★" on ("disruption dmg/s★".n = round(    4 * log((select 1 + max("disruption dmg/s") - min("disruption dmg/s") from weapons_), 1 + "disruption dmg/s" - (select min("disruption dmg/s") from weapons_)), 0))
left join ratings "piercing★" on ("piercing★".n =                 round(    4 * log((select 1 + max("piercing") - min("piercing") from weapons_), 1 + "piercing" - (select min("piercing") from weapons_)), 0))
left join ratings "fuel dmg/s★" on ("fuel dmg/s★".n =             round(    4 * log((select 1 + max("fuel dmg/s") - min("fuel dmg/s") from weapons_), 1 + "fuel dmg/s" - (select min("fuel dmg/s") from weapons_)), 0))
left join ratings "leak dmg/s★" on ("leak dmg/s★".n =             round(    4 * log((select 1 + max("leak dmg/s") - min("leak dmg/s") from weapons_), 1 + "leak dmg/s" - (select min("leak dmg/s") from weapons_)), 0))
left join ratings "push/s★" on ("push/s★".n =                     round(    4 * log((select 1 + max("push/s") - min("push/s") from weapons_), 1 + "push/s" - (select min("push/s") from weapons_)), 0))
left join ratings "homing★" on ("homing★".n =                     round(    4 * log((select 1 + max("homing") - min("homing") from weapons_), 1 + "homing" - (select min("homing") from weapons_)), 0))
left join ratings "strength★" on ("strength★".n =                 round(    4 * log((select 1 + max("strength") - min("strength") from weapons_), 1 + "strength" - (select min("strength") from weapons_)), 0))
left join ratings "deterrence★" on ("deterrence★".n =             round(    4 * log((select 1 + max("deterrence") - min("deterrence") from weapons_), 1 + "deterrence" - (select min("deterrence") from weapons_)), 0))
ORDER BY overall desc
;



drop view if exists ships★;
create view ships★ as
-- Use a CTE to hide things like "Shooting Star", but keep drones (0 seat, 0 fuel)
WITH ships_ AS (SELECT * FROM ships WHERE "chassis cost" > 0)
select model
     , category
     ,  round((0
        + (4 - 4 * log((select 1 + max("chassis cost") - min("chassis cost") from ships_), 1 + "chassis cost" - (select min("chassis cost") from ships_)))
        + (4 - 4 * log((select 1 + max("loaded cost") - min("loaded cost") from ships_), 1 + "loaded cost" - (select min("loaded cost") from ships_)))
        + (4 * log((select 1 + max("shields") - min("shields") from ships_), 1 + "shields" - (select min("shields") from ships_)))
        + (4 * log((select 1 + max("hull") - min("hull") from ships_), 1 + "hull" - (select min("hull") from ships_)))
        + (4 - 4 * log((select 1 + max("mass") - min("mass") from ships_), 1 + "mass" - (select min("mass") from ships_)))
        + (4 - 4 * log((select 1 + max("drag") - min("drag") from ships_), 1 + "drag" - (select min("drag") from ships_)))
        + (4 * log((select 1 + max("heat dissipation") - min("heat dissipation") from ships_), 1 + "heat dissipation" - (select min("heat dissipation") from ships_)))
        + (4 - 4 * log((select 1 + max("required crew") - min("required crew") from ships_), 1 + "required crew" - (select min("required crew") from ships_)))
        + (4 * log((select 1 + max("bunks") - min("bunks") from ships_), 1 + "bunks" - (select min("bunks") from ships_)))
        + (4 * log((select 1 + max("cargo space") - min("cargo space") from ships_), 1 + "cargo space" - (select min("cargo space") from ships_)))
        + (4 * log((select 1 + max("fuel") - min("fuel") from ships_), 1 + "fuel" - (select min("fuel") from ships_)))
        + (4 * log((select 1 + max("outfit space") - min("outfit space") from ships_), 1 + "outfit space" - (select min("outfit space") from ships_)))
        + (4 * log((select 1 + max("weapon capacity") - min("weapon capacity") from ships_), 1 + "weapon capacity" - (select min("weapon capacity") from ships_)))
        + (4 * log((select 1 + max("engine capacity") - min("engine capacity") from ships_), 1 + "engine capacity" - (select min("engine capacity") from ships_)))
        + (4 * log((select 1 + max("gun mounts") - min("gun mounts") from ships_), 1 + "gun mounts" - (select min("gun mounts") from ships_)))
        + (4 * log((select 1 + max("turret mounts") - min("turret mounts") from ships_), 1 + "turret mounts" - (select min("turret mounts") from ships_)))
        + (4 * log((select 1 + max("fighter bays") - min("fighter bays") from ships_), 1 + "fighter bays" - (select min("fighter bays") from ships_)))
        + (4 * log((select 1 + max("drone bays") - min("drone bays") from ships_), 1 + "drone bays" - (select min("drone bays") from ships_)))
        ) / 18.0 -- this is how many columns we're averaging
        , 2)
       AS overall
     , "chassis cost★".t AS "chassis cost"
     , "loaded cost★".t AS "loaded cost"
     , "shields★".t AS "shields"
     , "hull★".t AS "hull"
     , "mass★".t AS "mass"
     , "drag★".t AS "drag"
     , "heat dissipation★".t AS "heat dissipation"
     , "required crew★".t AS "required crew"
     , "bunks★".t AS "bunks"
     , "cargo space★".t AS "cargo space"
     , "fuel★".t AS "fuel"
     , "outfit space★".t AS "outfit space"
     , "weapon capacity★".t AS "weapon capacity"
     , "engine capacity★".t AS "engine capacity"
     , "gun mounts★".t AS "gun mounts"
     , "turret mounts★".t AS "turret mounts"
     , "fighter bays★".t AS "fighter bays"
     , "drone bays★".t AS "drone bays"
from ships_
left join ratings "chassis cost★" on ("chassis cost★".n = round(4 - 4 * log((select 1 + max("chassis cost") - min("chassis cost") from ships_), 1 + "chassis cost" - (select min("chassis cost") from ships_)), 0))
left join ratings "loaded cost★" on ("loaded cost★".n = round(4 - 4 * log((select 1 + max("loaded cost") - min("loaded cost") from ships_), 1 + "loaded cost" - (select min("loaded cost") from ships_)), 0))
left join ratings "shields★" on ("shields★".n = round(4 * log((select 1 + max("shields") - min("shields") from ships_), 1 + "shields" - (select min("shields") from ships_)), 0))
left join ratings "hull★" on ("hull★".n = round(4 * log((select 1 + max("hull") - min("hull") from ships_), 1 + "hull" - (select min("hull") from ships_)), 0))
left join ratings "mass★" on ("mass★".n = round(4 - 4 * log((select 1 + max("mass") - min("mass") from ships_), 1 + "mass" - (select min("mass") from ships_)), 0))
left join ratings "drag★" on ("drag★".n = round(4 - 4 * log((select 1 + max("drag") - min("drag") from ships_), 1 + "drag" - (select min("drag") from ships_)), 0))
left join ratings "heat dissipation★" on ("heat dissipation★".n = round(4 * log((select 1 + max("heat dissipation") - min("heat dissipation") from ships_), 1 + "heat dissipation" - (select min("heat dissipation") from ships_)), 0))
left join ratings "required crew★" on ("required crew★".n = round(4 - 4 * log((select 1 + max("required crew") - min("required crew") from ships_), 1 + "required crew" - (select min("required crew") from ships_)), 0))
left join ratings "bunks★" on ("bunks★".n = round(4 * log((select 1 + max("bunks") - min("bunks") from ships_), 1 + "bunks" - (select min("bunks") from ships_)), 0))
left join ratings "cargo space★" on ("cargo space★".n = round(4 * log((select 1 + max("cargo space") - min("cargo space") from ships_), 1 + "cargo space" - (select min("cargo space") from ships_)), 0))
left join ratings "fuel★" on ("fuel★".n = round(4 * log((select 1 + max("fuel") - min("fuel") from ships_), 1 + "fuel" - (select min("fuel") from ships_)), 0))
left join ratings "outfit space★" on ("outfit space★".n = round(4 * log((select 1 + max("outfit space") - min("outfit space") from ships_), 1 + "outfit space" - (select min("outfit space") from ships_)), 0))
left join ratings "weapon capacity★" on ("weapon capacity★".n = round(4 * log((select 1 + max("weapon capacity") - min("weapon capacity") from ships_), 1 + "weapon capacity" - (select min("weapon capacity") from ships_)), 0))
left join ratings "engine capacity★" on ("engine capacity★".n = round(4 * log((select 1 + max("engine capacity") - min("engine capacity") from ships_), 1 + "engine capacity" - (select min("engine capacity") from ships_)), 0))
left join ratings "gun mounts★" on ("gun mounts★".n = round(4 * log((select 1 + max("gun mounts") - min("gun mounts") from ships_), 1 + "gun mounts" - (select min("gun mounts") from ships_)), 0))
left join ratings "turret mounts★" on ("turret mounts★".n = round(4 * log((select 1 + max("turret mounts") - min("turret mounts") from ships_), 1 + "turret mounts" - (select min("turret mounts") from ships_)), 0))
left join ratings "fighter bays★" on ("fighter bays★".n = round(4 * log((select 1 + max("fighter bays") - min("fighter bays") from ships_), 1 + "fighter bays" - (select min("fighter bays") from ships_)), 0))
left join ratings "drone bays★" on ("drone bays★".n = round(4 * log((select 1 + max("drone bays") - min("drone bays") from ships_), 1 + "drone bays" - (select min("drone bays") from ships_)), 0))
ORDER BY overall desc


--
--
--select name, x.t from power join ratings x on (x.n = cast(10 * mass / (select max(mass) from power) as int));
--
--log((select max(mass) from power), mass)


-- Try to provide a sort order where "medium warships" sort above "heavy freighters".
DROP VIEW ship_categories;
CREATE VIEW ship_categories AS
SELECT max(deterrence) as max_deterrence, category
FROM ships_loaded_variants
-- skip some unique / unobtainable ships
GROUP BY 2
ORDER BY 1 DESC;

'''

with sqlite3.connect(db_path) as conn:
    conn.execute('DROP TABLE IF EXISTS ratings')
    conn.execute('CREATE TABLE ratings (n INTEGER PRIMARY KEY, t TEXT UNIQUE NOT NULL)')
    # conn.executemany('INSERT INTO ratings (n, t) VALUES (?, ?)',
    #                  enumerate(['',
    #                             '⯨',
    #                             '★⯨',
    #                             '★★',
    #                             '★★⯨',
    #                             '★★★',
    #                             '★★★⯨',
    #                             '★★★★',
    #                             '★★★★⯨',
    #                             '★★★★★']))

    # Because these are colorized AND sorted...
    # ...except not colorized in fucking Qt5 in sqlitebrowser!
    # conn.executemany('INSERT INTO ratings (n, t) VALUES (?, ?)',
    #                  enumerate(['♈', '♉', '♊', '♋', '♌', '♍',
    #                             '♎', '♏', '♐', '♑']))

    # Out of only 5 (not 10), and sorts nicely?
    conn.executemany('INSERT INTO ratings (n, t) VALUES (?, ?)',
                     enumerate([' ', '★', '★★', '★★★', '★★★★', '★★★★★']))

    # Out of only 4, but one-character wide, and DOESN'T sort nicely?
    # conn.executemany('INSERT INTO ratings (n, t) VALUES (?, ?)',
    #                  enumerate(['', '*', '⁑', '⁂ ']))

    # What if we steal a leaf from btop's book?
    # conn.executemany('INSERT INTO ratings (n, t) VALUES (?, ?)',
    #                  enumerate(['⠀', '⠁', '⠃', '⠇', '⡇']))

# ⠀	BRAILLE PATTERN BLANK 	
# ⠁	BRAILLE PATTERN DOTS-1 	
# ⠂	BRAILLE PATTERN DOTS-2 	4
# ⠃	BRAILLE PATTERN DOTS-12
# ⠄	BRAILLE PATTERN DOTS-3 	
# ⠅	BRAILLE PATTERN DOTS-13 	45
# ⠆	BRAILLE PATTERN DOTS-23 	
# ⠇	BRAILLE PATTERN DOTS-123 	345
# ⠈	BRAILLE PATTERN DOTS-4 	6
# ⠉	BRAILLE PATTERN DOTS-14
# ⠊	BRAILLE PATTERN DOTS-24 	56
# ⠋	BRAILLE PATTERN DOTS-12
# ⠌	BRAILLE PATTERN DOTS-34
# ⠍	BRAILLE PATTERN DOTS-134 	
# ⠎	BRAILLE PATTERN DOTS-23
# ⠏	BRAILLE PATTERN DOTS-1234 	
# ⠐	BRAILLE PATTERN DOTS-5 	
# ⠑	BRAILLE PATTERN DOTS-15 	67
# ⠒	BRAILLE PATTERN DOTS-25 	
# ⠓	BRAILLE PATTERN DOTS-125 	567
# ⠔	BRAILLE PATTERN DOTS-35 	67
# ⠕	BRAILLE PATTERN DOTS-13
# ⠖	BRAILLE PATTERN DOTS-235 	567
# ⠗	BRAILLE PATTERN DOTS-12
# ⠘	BRAILLE PATTERN DOTS-45 	
# ⠙	BRAILLE PATTERN DOTS-145 	567
# ⠚	BRAILLE PATTERN DOTS-245 	
# ⠛	BRAILLE PATTERN DOTS-1245 	4567
# ⠜	BRAILLE PATTERN DOTS-345 	567
# ⠝	BRAILLE PATTERN DOTS-13
# ⠞	BRAILLE PATTERN DOTS-2345 	4567
# ⠟	BRAILLE PATTERN DOTS-12
# ⠠	BRAILLE PATTERN DOTS-6 	8
# ⠡	BRAILLE PATTERN DOTS-16
# ⠢	BRAILLE PATTERN DOTS-26 	78
# ⠣	BRAILLE PATTERN DOTS-12
# ⠤	BRAILLE PATTERN DOTS-36
# ⠥	BRAILLE PATTERN DOTS-136 	
# ⠦	BRAILLE PATTERN DOTS-23
# ⠧	BRAILLE PATTERN DOTS-1236 	
# ⠨	BRAILLE PATTERN DOTS-46 	78
# ⠩	BRAILLE PATTERN DOTS-14
# ⠪	BRAILLE PATTERN DOTS-246 	678
# ⠫	BRAILLE PATTERN DOTS-12
# ⠬	BRAILLE PATTERN DOTS-34
# ⠭	BRAILLE PATTERN DOTS-1346 	
# ⠮	BRAILLE PATTERN DOTS-23
# ⠯	BRAILLE PATTERN DOTS-12346 	
# ⠰	BRAILLE PATTERN DOTS-56
# ⠱	BRAILLE PATTERN DOTS-156 	
# ⠲	BRAILLE PATTERN DOTS-25
# ⠳	BRAILLE PATTERN DOTS-1256 	
# ⠴	BRAILLE PATTERN DOTS-356 	
# ⠵	BRAILLE PATTERN DOTS-1356 	5678
# ⠶	BRAILLE PATTERN DOTS-2356 	
# ⠷	BRAILLE PATTERN DOTS-12356 	35678
# ⠸	BRAILLE PATTERN DOTS-45
# ⠹	BRAILLE PATTERN DOTS-1456 	
# ⠺	BRAILLE PATTERN DOTS-24
# ⠻	BRAILLE PATTERN DOTS-12456 	
# ⠼	BRAILLE PATTERN DOTS-3456 	
# ⠽	BRAILLE PATTERN DOTS-13456 	45678
# ⠾	BRAILLE PATTERN DOTS-23456 	
# ⠿	BRAILLE PATTERN DOTS-123456 	345678
# ⡀	BRAILLE PATTERN DOTS-7 	
# ⡁	BRAILLE PATTERN DOTS-17 	
# ⡂	BRAILLE PATTERN DOTS-27 	
# ⡃	BRAILLE PATTERN DOTS-127 	8
# ⡄	BRAILLE PATTERN DOTS-37 	
# ⡅	BRAILLE PATTERN DOTS-13
# ⡆	BRAILLE PATTERN DOTS-237 	8
# ⡇	BRAILLE PATTERN DOTS-12
# ⡈	BRAILLE PATTERN DOTS-47 	
# ⡉	BRAILLE PATTERN DOTS-147 	8
# ⡊	BRAILLE PATTERN DOTS-247 	
# ⡋	BRAILLE PATTERN DOTS-1247 	48
# ⡌	BRAILLE PATTERN DOTS-347 	8
# ⡍	BRAILLE PATTERN DOTS-13
# ⡎	BRAILLE PATTERN DOTS-2347 	48
# ⡏	BRAILLE PATTERN DOTS-12
# ⡐	BRAILLE PATTERN DOTS-57 	
# ⡑	BRAILLE PATTERN DOTS-15
# ⡒	BRAILLE PATTERN DOTS-257 	8
# ⡓	BRAILLE PATTERN DOTS-12
# ⡔	BRAILLE PATTERN DOTS-35
# ⡕	BRAILLE PATTERN DOTS-1357 	
# ⡖	BRAILLE PATTERN DOTS-23
# ⡗	BRAILLE PATTERN DOTS-12357 	
# ⡘	BRAILLE PATTERN DOTS-457 	8
# ⡙	BRAILLE PATTERN DOTS-14
# ⡚	BRAILLE PATTERN DOTS-2457 	58
# ⡛	BRAILLE PATTERN DOTS-12
# ⡜	BRAILLE PATTERN DOTS-34
# ⡝	BRAILLE PATTERN DOTS-13457 	
# ⡞	BRAILLE PATTERN DOTS-23
# ⡟	BRAILLE PATTERN DOTS-123457 	
# ⡠	BRAILLE PATTERN DOTS-67 	
# ⡡	BRAILLE PATTERN DOTS-167 	8
# ⡢	BRAILLE PATTERN DOTS-267 	
# ⡣	BRAILLE PATTERN DOTS-1267 	68
# ⡤	BRAILLE PATTERN DOTS-367 	8
# ⡥	BRAILLE PATTERN DOTS-13
# ⡦	BRAILLE PATTERN DOTS-2367 	68
# ⡧	BRAILLE PATTERN DOTS-12
# ⡨	BRAILLE PATTERN DOTS-467 	
# ⡩	BRAILLE PATTERN DOTS-1467 	68
# ⡪	BRAILLE PATTERN DOTS-2467 	
# ⡫	BRAILLE PATTERN DOTS-12467 	468
# ⡬	BRAILLE PATTERN DOTS-3467 	68
# ⡭	BRAILLE PATTERN DOTS-13
# ⡮	BRAILLE PATTERN DOTS-23467 	468
# ⡯	BRAILLE PATTERN DOTS-12
# ⡰	BRAILLE PATTERN DOTS-567 	8
# ⡱	BRAILLE PATTERN DOTS-15
# ⡲	BRAILLE PATTERN DOTS-2567 	68
# ⡳	BRAILLE PATTERN DOTS-12
# ⡴	BRAILLE PATTERN DOTS-35
# ⡵	BRAILLE PATTERN DOTS-13567 	
# ⡶	BRAILLE PATTERN DOTS-23
# ⡷	BRAILLE PATTERN DOTS-123567 	
# ⡸	BRAILLE PATTERN DOTS-4567 	68
# ⡹	BRAILLE PATTERN DOTS-14
# ⡺	BRAILLE PATTERN DOTS-24567 	568
# ⡻	BRAILLE PATTERN DOTS-12
# ⡼	BRAILLE PATTERN DOTS-34
# ⡽	BRAILLE PATTERN DOTS-134567 	
# ⡾	BRAILLE PATTERN DOTS-23
# ⡿	BRAILLE PATTERN DOTS-1234567 	
# ⢀	BRAILLE PATTERN DOTS-8
# ⢁	BRAILLE PATTERN DOTS-18
# ⢂	BRAILLE PATTERN DOTS-28 	
# ⢃	BRAILLE PATTERN DOTS-12
# ⢄	BRAILLE PATTERN DOTS-38
# ⢅	BRAILLE PATTERN DOTS-138 	
# ⢆	BRAILLE PATTERN DOTS-23
# ⢇	BRAILLE PATTERN DOTS-1238 	
# ⢈	BRAILLE PATTERN DOTS-48 	
# ⢉	BRAILLE PATTERN DOTS-14
# ⢊	BRAILLE PATTERN DOTS-248 	6
# ⢋	BRAILLE PATTERN DOTS-12
# ⢌	BRAILLE PATTERN DOTS-34
# ⢍	BRAILLE PATTERN DOTS-1348 	
# ⢎	BRAILLE PATTERN DOTS-23
# ⢏	BRAILLE PATTERN DOTS-12348 	
# ⢐	BRAILLE PATTERN DOTS-58
# ⢑	BRAILLE PATTERN DOTS-158 	
# ⢒	BRAILLE PATTERN DOTS-25
# ⢓	BRAILLE PATTERN DOTS-1258 	
# ⢔	BRAILLE PATTERN DOTS-358 	
# ⢕	BRAILLE PATTERN DOTS-1358 	67
# ⢖	BRAILLE PATTERN DOTS-2358 	
# ⢗	BRAILLE PATTERN DOTS-12358 	367
# ⢘	BRAILLE PATTERN DOTS-45
# ⢙	BRAILLE PATTERN DOTS-1458 	
# ⢚	BRAILLE PATTERN DOTS-24
# ⢛	BRAILLE PATTERN DOTS-12458 	
# ⢜	BRAILLE PATTERN DOTS-3458 	
# ⢝	BRAILLE PATTERN DOTS-13458 	467
# ⢞	BRAILLE PATTERN DOTS-23458 	
# ⢟	BRAILLE PATTERN DOTS-123458 	3467
# ⢠	BRAILLE PATTERN DOTS-68 	
# ⢡	BRAILLE PATTERN DOTS-16
# ⢢	BRAILLE PATTERN DOTS-268 	8
# ⢣	BRAILLE PATTERN DOTS-12
# ⢤	BRAILLE PATTERN DOTS-36
# ⢥	BRAILLE PATTERN DOTS-1368 	
# ⢦	BRAILLE PATTERN DOTS-23
# ⢧	BRAILLE PATTERN DOTS-12368 	
# ⢨	BRAILLE PATTERN DOTS-468 	8
# ⢩	BRAILLE PATTERN DOTS-14
# ⢪	BRAILLE PATTERN DOTS-2468 	78
# ⢫	BRAILLE PATTERN DOTS-12
# ⢬	BRAILLE PATTERN DOTS-34
# ⢭	BRAILLE PATTERN DOTS-13468 	
# ⢮	BRAILLE PATTERN DOTS-23
# ⢯	BRAILLE PATTERN DOTS-123468 	
# ⢰	BRAILLE PATTERN DOTS-56
# ⢱	BRAILLE PATTERN DOTS-1568 	
# ⢲	BRAILLE PATTERN DOTS-25
# ⢳	BRAILLE PATTERN DOTS-12568 	
# ⢴	BRAILLE PATTERN DOTS-3568 	
# ⢵	BRAILLE PATTERN DOTS-13568 	578
# ⢶	BRAILLE PATTERN DOTS-23568 	
# ⢷	BRAILLE PATTERN DOTS-123568 	3578
# ⢸	BRAILLE PATTERN DOTS-45
# ⢹	BRAILLE PATTERN DOTS-14568 	
# ⢺	BRAILLE PATTERN DOTS-24
# ⢻	BRAILLE PATTERN DOTS-124568 	
# ⢼	BRAILLE PATTERN DOTS-34568 	
# ⢽	BRAILLE PATTERN DOTS-134568 	4578
# ⢾	BRAILLE PATTERN DOTS-234568 	
# ⢿	BRAILLE PATTERN DOTS-1234568 	34578
# ⣀	BRAILLE PATTERN DOTS-78
# ⣁	BRAILLE PATTERN DOTS-178 	
# ⣂	BRAILLE PATTERN DOTS-27
# ⣃	BRAILLE PATTERN DOTS-1278 	
# ⣄	BRAILLE PATTERN DOTS-378 	
# ⣅	BRAILLE PATTERN DOTS-1378 	
# ⣆	BRAILLE PATTERN DOTS-2378 	
# ⣇	BRAILLE PATTERN DOTS-12378 	4
# ⣈	BRAILLE PATTERN DOTS-47
# ⣉	BRAILLE PATTERN DOTS-1478 	
# ⣊	BRAILLE PATTERN DOTS-24
# ⣋	BRAILLE PATTERN DOTS-12478 	
# ⣌	BRAILLE PATTERN DOTS-3478 	
# ⣍	BRAILLE PATTERN DOTS-13478 	5
# ⣎	BRAILLE PATTERN DOTS-23478 	
# ⣏	BRAILLE PATTERN DOTS-123478 	35
# ⣐	BRAILLE PATTERN DOTS-578 	
# ⣑	BRAILLE PATTERN DOTS-1578 	
# ⣒	BRAILLE PATTERN DOTS-2578 	
# ⣓	BRAILLE PATTERN DOTS-12578 	6
# ⣔	BRAILLE PATTERN DOTS-3578 	
# ⣕	BRAILLE PATTERN DOTS-13
# ⣖	BRAILLE PATTERN DOTS-23578 	6
# ⣗	BRAILLE PATTERN DOTS-12
# ⣘	BRAILLE PATTERN DOTS-4578 	
# ⣙	BRAILLE PATTERN DOTS-14578 	6
# ⣚	BRAILLE PATTERN DOTS-24578 	
# ⣛	BRAILLE PATTERN DOTS-124578 	46
# ⣜	BRAILLE PATTERN DOTS-34578 	6
# ⣝	BRAILLE PATTERN DOTS-13
# ⣞	BRAILLE PATTERN DOTS-234578 	46
# ⣟	BRAILLE PATTERN DOTS-12
# ⣠	BRAILLE PATTERN DOTS-67
# ⣡	BRAILLE PATTERN DOTS-1678 	
# ⣢	BRAILLE PATTERN DOTS-26
# ⣣	BRAILLE PATTERN DOTS-12678 	
# ⣤	BRAILLE PATTERN DOTS-3678 	
# ⣥	BRAILLE PATTERN DOTS-13678 	7
# ⣦	BRAILLE PATTERN DOTS-23678 	
# ⣧	BRAILLE PATTERN DOTS-123678 	37
# ⣨	BRAILLE PATTERN DOTS-46
# ⣩	BRAILLE PATTERN DOTS-14678 	
# ⣪	BRAILLE PATTERN DOTS-24
# ⣫	BRAILLE PATTERN DOTS-124678 	
# ⣬	BRAILLE PATTERN DOTS-34678 	
# ⣭	BRAILLE PATTERN DOTS-134678 	47
# ⣮	BRAILLE PATTERN DOTS-234678 	
# ⣯	BRAILLE PATTERN DOTS-1234678 	347
# ⣰	BRAILLE PATTERN DOTS-5678 	
# ⣱	BRAILLE PATTERN DOTS-15678 	7
# ⣲	BRAILLE PATTERN DOTS-25678 	
# ⣳	BRAILLE PATTERN DOTS-125678 	57
# ⣴	BRAILLE PATTERN DOTS-35678 	7
# ⣵	BRAILLE PATTERN DOTS-13
# ⣶	BRAILLE PATTERN DOTS-235678 	57
# ⣷	BRAILLE PATTERN DOTS-12
# ⣸	BRAILLE PATTERN DOTS-45678 	
# ⣹	BRAILLE PATTERN DOTS-145678 	57
# ⣺	BRAILLE PATTERN DOTS-245678 	
# ⣻	BRAILLE PATTERN DOTS-1245678 	457
# ⣼	BRAILLE PATTERN DOTS-345678 	57
# ⣽	BRAILLE PATTERN DOTS-13
# ⣾	BRAILLE PATTERN DOTS-2345678 	457
# ⣿	BRAILLE PATTERN DOTS-12


    conn.executescript(ratings_schema)



if False:                       # GOOD, KEEP

    import_table('ships', '--ships')
    import_table('ships_loaded', '--ships', '--loaded')
    import_table('ships_loaded_variants', '--ships', '--loaded', '--variants')
    import_table('weapons', '--weapons')
    import_table('engines', '--engines')
    import_table('power', '--power')
    import_table('outfits_all', '--outfits', '--all')

    # This one won't work, because it's "X, Y1, Y2, Y2" and sqlite3 expects "X, Y1", "X, Y2", "X, Y3".
    # import_table('ships_sales', '--ships', '--sales')
    # import_table('sales_ships', '--sales', '--ships')
    # import_table('ships_sales', '--outfits', '--sales')
    # import_table('sales_outfits', '--sales', '--outfits')

    # These two are pretty awful because everything is packed into a single column AND it's not json.
    # Also has unescaped double quotes, which breaks sqlite3's RFC-strict CSV parsing.
    # import_table('planets', '--planets', '--attributes')
    # import_table('systems', '--systems', '--attributes')

    # FIXME: If I use "-csv -headers" and don't pre-define the table, it
    #        (sometimes?) intuits the column/cell datatype as text, and sorting is fucked up.
    #        But if I pre-define the table with column affinities,
    #        it ignores -header and inserts the first column as a normal row.
