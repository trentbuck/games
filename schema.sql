-- -*- sql-product: sqlite -*-
PRAGMA journal_mode = wal;
DROP TABLE IF EXISTS games;
CREATE TABLE games (id INTEGER PRIMARY KEY, rating REAL, price INTEGER, time INTEGER, name TEXT);


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
       id,
       name
FROM games_fudged
ORDER BY rating_fudged / (1.0 + (time_fudged / 60.0)) DESC;


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
             id,
             name
      FROM games_fudged
      WHERE price > 0
      ORDER BY Δ DESC)
-- Don't even mention games that are already below the average.
-- UGH can't just do "SELECT steamdb_price_per_hour FROM stats" because that's pretty-printed.
WHERE "$/hour (steamdb)" > (SELECT steamdb_average_price_per_hour FROM stats);



CREATE TABLE IF NOT EXISTS howlongtobeat (
    game_id INTEGER PRIMARY KEY,
    game_name TEXT NOT NULL,
    profile_steam INTEGER UNIQUE REFERENCES games (id),
    comp_main INTEGER,          -- Main Story (in seconds)
    comp_plus INTEGER,          -- Main + Sides (in seconds)
    comp_100 INTEGER,           -- Completionist (in seconds)
    comp_all INTEGER);          -- All Styles (in seconds)
