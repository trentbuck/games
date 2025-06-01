-- -*- sql-product: sqlite -*-
PRAGMA journal_mode = wal;
DROP TABLE IF EXISTS games;
CREATE TABLE games (id INTEGER PRIMARY KEY, rating REAL, price INTEGER, time INTEGER, name TEXT);


-- FIXME: add this to stats:
-- with cte1 as (select sum(time)/60.0 as total_hours, julianday() - julianday('2018-02-18') as days_since_account_created from games)
-- select round(total_hours / days_since_account_created, 1) as average_hours_per_day_in_steam, * from cte1;

CREATE VIEW IF NOT EXISTS stats AS
SELECT (sum(time / 60.0)) AS total_playtime,
       (avg(time / 60.0)) AS average_playtime,
       (sum(price / 100)) AS total_spent,  -- at today's prices
       (avg(price / 100.0)) AS average_price,
       -- "Average price calculation only includes games that have a price"
       (avg(CASE WHEN price >0 THEN price ELSE NULL END / 100.0)) AS steamdb_average_price,
       (sum(price / 100.0) / sum(time / 60.0)) AS price_per_hour,
       (avg((price / 100.0) / max(1.0, (time / 60.0)))) AS average_price_per_hour,
       -- "Average price calculation only includes games that have a price"
       (avg((CASE WHEN price >0 THEN price ELSE NULL END / 100.0) / max(1.0, (time / 60.0)))) AS steamdb_average_price_per_hour
FROM games;

CREATE VIEW IF NOT EXISTS stats_text AS
SELECT printf('%.2f hours', total_playtime) AS total_playtime,
       printf('%.2f hours', average_playtime) AS average_playtime,
       printf('%i A$', total_spent) AS total_spent,  -- at today's prices
       printf('%.2f A$', average_price) AS average_price,
       -- "Average price calculation only includes games that have a price"
       printf('%.2f A$', steamdb_average_price) AS steamdb_average_price,
       printf('%.2f A$/hour', price_per_hour) AS price_per_hour,
       printf('%.2f A$/hour', average_price_per_hour) AS average_price_per_hour,
       -- "Average price calculation only includes games that have a price"
       printf('%.2f A$/hour', steamdb_average_price_per_hour) AS steamdb_average_price_per_hour
FROM stats;



-- Upstream already offers a dollars-per-hour sort.
-- In many cases this is a good heuristic:
--   * a $50 game should give you 10 hours of fun;
--   * a $5 game should give you 1 hour of fun.
-- It falls apart around the edges; because e.g.
--   * different genres have different replay value
--     (e.g. Civilization 6 vs. Far Cry 6)
--   * some stuff is massively overpriced,
--     e.g. Darius Burst, Call of Duty
--
-- What about if we instead say:
--   * a 90%-rated game should give lots of fun
--   * a 60%-rated game should give some fun
--   * a 20%-rated game shouldn't give much fun at all
--
-- Let's look for high-rated low-playtime games.


-- FIXME...
-- "If game A has 80% score, and game B has 90% score, you should play game B *TWICE* as much, not 10% more."
-- i.e. treat score as a log scale not linear scale.
-- sqlite supports log/exponential functions: https://www.sqlite.org/lang_mathfunc.html
-- But Debian disables them:
--     sqlite3 '' 'select log(1)'
--     ⇒ Error: no such function: log
--     python3 -c 'import sqlite3; print(sqlite3.connect(":memory:").execute("select log(1)").fetchall())'
--     ⇒ python3 -c 'import sqlite3; print(sqlite3.connect(":memory:").execute("select log(1)").fetchall())'


CREATE VIEW IF NOT EXISTS games_fudged AS
SELECT -- If there is no rating, guess it is 70%.
       -- sqlite> SELECT min(rating), avg(rating), max(rating) FROM games;
       -- min(rating) = 19.47
       -- avg(rating) = 72.3078166550039
       -- max(rating) = 97.7
       -- sqlite>  SELECT min(rating), avg(rating), max(rating) FROM games WHERE price;
       -- min(rating) = 19.47
       -- avg(rating) = 79.1609375000002
       -- max(rating) = 97.7
       CASE WHEN rating IS NULL then 70.0 ELSE rating END AS rating_fudged,  -- avg rating is ~72%
       --- 1 minute approximates "unplayed" but avoids divide-by-zero issues
       CASE WHEN time IS NULL then 1.0 ELSE time END as time_fudged,
       *
FROM games;


-- We don't want hyperbola when time is less than 1.0 hours.
--   https://en.wikipedia.org/wiki/Division_by_zero#/media/File:Hyperbola_one_over_x.svg
-- Therefore simply add 1.0 to all quotients.
-- Don't do the more intuitive max(1 hour, time), as that
-- would require me to spend a full hour on a game to get it off the top of the list.
CREATE VIEW IF NOT EXISTS what_game_next AS
SELECT rating,
       printf('%.2f', rating_fudged / (1.0 + (time_fudged / 60.0))) AS "rating/hour",
       CASE WHEN price THEN printf(price / 100.0) ELSE NULL END AS "$",
       CASE WHEN price >0 THEN printf('%.2f', (price / 100.0) / (time_fudged / 60.0)) ELSE NULL END "$/hour",
       CASE WHEN price >0 THEN printf('%.2f', (price / 100.0) / max(1.0, (time_fudged / 60.0))) ELSE NULL END AS "$/hour (steamdb)",
       CASE
         WHEN time >1440 THEN printf('%.2f days', time / 1440.0)
         WHEN time >60 THEN printf('%.2f hours', time  / 60.0)
         WHEN time >0 THEN printf('%i min', time)
       END AS time,
       CASE WHEN comp_all IS NULL THEN NULL ELSE printf('%.2f hours', comp_all / 3600.0) END AS hltb,
       id,
       name
FROM games_fudged
LEFT JOIN howlongtobeat ON (id = profile_steam)
ORDER BY rating_fudged / (1.0 + (time_fudged / 60.0)) DESC;


-- Because dealing with printf'd fields in sqlitebrowser is a shitshow.
CREATE VIEW IF NOT EXISTS what_game_next_numeric AS
SELECT cast(round(rating) as int) AS rating,
       -- This is a simple scale where playing for 1 hour halves its rating.
       -- This meant stuff with very long playtimes went to the very bottom, even though
       -- a 90% rated game with 100 hours is probably still more fun to REPLAY than a 20% rated game with 0.5 hours.
       -- Here is a synthetic example:
       --  sqlite> create temporary table games_fudged (time_fudged I, rating I, name S);
       --  sqlite> insert into games_fudged values (0, 90, 'great unplayed game'), (100*60, 90, 'great finished game'), (60, 90, 'great started game'), (0, 70, 'good unplayed game'), (100*60, 70, 'good finished game'), (60, 70, 'good started game'), (0, 30, 'trash unplayed game'), (100*60, 30, 'trash finished game'), (60, 90, 'trash started game');
       --  sqlite> update games_fudged set rating = 30 where name like 'trash%';
       --  sqlite> update games_fudged set time_fudged = 6 where name like '%started%'; -- 6 minutes, not 60 minutes
       --  sqlite> select new-old as "δ", * from (select rating, round(rating/(1+log(60, 1+time_fudged)), 1) AS "new", round(rating/(1.0 + time_fudged/60.0), 1) as old, round(time_fudged/60.0, 1) as h, name from games_fudged) order by new desc;
       --  δ      rating  new   old   h      name
       --  -----  ------  ----  ----  -----  -------------------
       --  0.0    90      90.0  90.0  0.0    great unplayed game
       --  0.0    70      70.0  70.0  0.0     good unplayed game
       --  -20.8  90      61.0  81.8  0.1    great started game
       --  -16.2  70      47.4  63.6  0.1     good started game
       --  0.0    30      30.0  30.0  0.0    trash unplayed game
       --  27.9   90      28.8  0.9   100.0  great finished game
       --  21.7   70      22.4  0.7   100.0   good finished game
       --  -7.0   30      20.3  27.3  0.1    trash started game
       --  9.3    30      9.6   0.3   100.0  trash finished game

       -- And using real data as examples (trying to pick {good,ok,shit} {unplayed,finished,played-to-death}):
       -- sqlite>select new-old as "δ", * from (select cast(rating_fudged as int) as rating, round(rating_fudged/(1+log(60, 1+time_fudged)), 1) AS "new", round(rating_fudged/(1.0 + time_fudged/60.0), 1) as old, round(time_fudged/60.0,1) as h, name from games_fudged where name in ('Fallout 4', 'Portal 2', 'Syberia 2', 'Just Cause 4', 'ZOMBI', 'Home', 'Arma Tactics', 'Sacred 3', 'Stranded')) order by old desc;
       -- δ      rating  new   old   h       name
       -- -----  ------  ----  ----  ------  ------------
       -- -10.6  82      70.9  81.5  0.0     Syberia 2
       -- -7.3   65      35.1  42.4  0.5     Home
       -- -5.0   38      33.0  38.0  0.0     Stranded
       -- 30.1   97      37.3  7.2   12.7    Portal 2
       -- 18.9   62      24.3  5.4   10.7    ZOMBI
       -- 8.2    28      11.4  3.2   7.9     Sacred 3
       -- 11.0   34      12.3  1.3   25.4    Arma Tactics
       -- 19.3   61      20.1  0.8   71.0    Just Cause 4
       -- 22.0   82      22.1  0.1   1167.5  Fallout 4
       -- sqlite> select new-old as "δ", * from (select cast(rating_fudged as int) as rating, round(rating_fudged/(1+log(60, 1+time_fudged)), 1) AS "new", round(rating_fudged/(1.0 + time_fudged/60.0), 1) as old, round(time_fudged/60.0,1) as h, name from games_fudged where name in ('Fallout 4', 'Portal 2', 'Syberia 2', 'Just Cause 4', 'ZOMBI', 'Home', 'Arma Tactics', 'Sacred 3', 'Stranded')) order by new desc;
       -- δ      rating  new   old   h       name
       -- -----  ------  ----  ----  ------  ------------
       -- -10.6  82      70.9  81.5  0.0     Syberia 2
       -- 30.1   97      37.3  7.2   12.7    Portal 2
       -- -7.3   65      35.1  42.4  0.5     Home
       -- -5.0   38      33.0  38.0  0.0     Stranded
       -- 18.9   62      24.3  5.4   10.7    ZOMBI
       -- 22.0   82      22.1  0.1   1167.5  Fallout 4
       -- 19.3   61      20.1  0.8   71.0    Just Cause 4
       -- 11.0   34      12.3  1.3   25.4    Arma Tactics
       -- 8.2    28      11.4  3.2   7.9     Sacred 3

       -- round(rating_fudged/(1.0 + time_fudged/60.0), 1) AS "rating/h",
       round(rating_fudged/(1.0 + log(60, time_fudged)), 1) AS "rating/h",
       CASE WHEN price THEN cast(round(price/100.0) as int) END AS "$",
       CASE WHEN price THEN cast(round(price / 100.0 / (1.0 + time_fudged / 60.0)) as int) END AS "$/h",
       round(time/60.0, 1) AS h,
       CASE WHEN comp_all THEN cast(round(comp_all/3600.0) as int) END AS hltb,
       CASE WHEN time AND comp_all THEN round((time/60.0)/(comp_all/3600.0), 2) END AS "done?",
       id,
       name
FROM games_fudged
LEFT JOIN howlongtobeat ON (id=profile_steam)
ORDER BY "rating/h" DESC;


CREATE VIEW IF NOT EXISTS what_game_next_numeric_nonfree AS
SELECT * FROM what_game_next_numeric WHERE "$" IS NOT NULL;


-- What games, after 1 hour more play, will most improve (lower) by "Average price per hour" KPI?
CREATE VIEW IF NOT EXISTS what_game_next_to_lower_my_KPI AS
SELECT *
FROM (SELECT round((CASE WHEN price >0 THEN price ELSE NULL END / 100.0) / max(1.0, (time / 60.0)), 2) AS "$/hour (steamdb)",
             round(
               ((1.0 * (price / 100.0) / max(1.0, (time_fudged / 60.0))) -
                (1.0 * (price / 100.0) / max(1.0, (time_fudged / 60.0) + 1))),
               2) AS Δ,
             rating,
             CASE WHEN price THEN printf(price / 100.0) ELSE NULL END AS "$",
             CASE
               WHEN time >1440 THEN printf('%.2f days', time / 1440.0)
               WHEN time >60 THEN printf('%.2f hours', time  / 60.0)
               WHEN time >0 THEN printf('%i min', time)
             END AS time,
             CASE WHEN comp_all IS NULL THEN NULL ELSE printf('%.2f hours', comp_all / 3600.0) END AS hltb,
             id,
             name
      FROM games_fudged
      LEFT JOIN howlongtobeat ON (id = profile_steam)
      WHERE price > 0
      ORDER BY Δ DESC)
-- Don't even mention games that are already below the average.
-- UGH can't just do "SELECT steamdb_price_per_hour FROM stats" because that's pretty-printed.
WHERE "$/hour (steamdb)" > (SELECT steamdb_average_price_per_hour FROM stats);



-- bash5$ sqlite3 -header -csv all-games.db "SELECT CAST(round(100.0*time_fudged/(comp_main/60.0)) AS INTEGER) AS completion_percentage, rating_fudged, name FROM games_fudged JOIN howlongtobeat ON (id = profile_steam) ORDER BY 1 DESC, 2 DESC" >games-by-my-completion.csv
CREATE TABLE IF NOT EXISTS howlongtobeat (
    game_id INTEGER PRIMARY KEY,
    game_name TEXT NOT NULL,
    profile_steam INTEGER UNIQUE REFERENCES games (id),
    comp_main INTEGER,          -- Main Story (in seconds)
    comp_plus INTEGER,          -- Main + Sides (in seconds)
    comp_100 INTEGER,           -- Completionist (in seconds)
    comp_all INTEGER);          -- All Styles (in seconds)
