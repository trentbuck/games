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


CREATE VIEW IF NOT EXISTS what_game_next AS
SELECT rating_fudged / (time_fudged / 60.0) AS rating_per_hour,
       rating_fudged / max(1.0, (time_fudged / 60.0)) AS rating_per_hour_rounded_up,
       (price / 100.0) / (time_fudged / 60.0) AS price_per_hour,
       (price / 100.0) / max(1.0, (time / 60.0)) AS steamdb_price_per_hour,
       -- What games, after 1 hour more play, will most improve (lower) by "Average price per hour" KPI?
       ((1.0*price/max(1.0, time_fudged)) -
        (1.0*price/max(1.0, time_fudged + 1))) AS price_per_hour_change_after_1h_more_play,
       *
FROM games_fudged
ORDER BY rating_per_hour DESC;


-- What games, after 1 hour more play, will most improve (lower) by "Average price per hour" KPI?
CREATE VIEW IF NOT EXISTS what_game_next_to_lower_my_KPI AS
SELECT *
FROM (SELECT ((CASE WHEN price >0 THEN price ELSE NULL END / 100.0) / max(1.0, (time / 60.0))) AS steamdb_price_per_hour,
             ((1.0 * (price / 100.0) / max(1.0, (time_fudged / 60.0))) -
              (1.0 * (price / 100.0) / max(1.0, (time_fudged / 60.0) + 1))) AS change,
             *
      FROM games_fudged
      WHERE price > 0
      ORDER BY change DESC)
-- Don't even mention games that are already below the average.
-- UGH can't just do "SELECT steamdb_price_per_hour FROM stats" because that's pretty-printed.
WHERE NOT steamdb_price_per_hour < (SELECT steamdb_average_price_per_hour FROM stats);
