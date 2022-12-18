#!/usr/bin/python3
import pathlib
import datetime
import argparse
import subprocess
import sqlite3

import lxml.html
import lxml.etree


def mystrip(s: str, prefix=None, suffix=None) -> str:
    if prefix:
        assert s.startswith(prefix)
        s = s[len(prefix):]
    if suffix:
        assert s.endswith(suffix)
        s = s[:-len(suffix)]
    return s


parser = argparse.ArgumentParser()
parser.add_argument(
    'url',
    nargs='?',
    default='https://steamdb.info/calculator/76561198815748328/?cc=au&all_games')
args = parser.parse_args()
html_path = pathlib.Path('all-games.html')
db_path = pathlib.Path('all-games.db')


try:
    if datetime.datetime.fromtimestamp(html_path.stat().st_mtime) < datetime.datetime.now() - datetime.timedelta(days=7):
        raise FileNotFoundError('too old', html_path)
except FileNotFoundError:
    # File doesn't exist, or is over a week old.
    subprocess.check_call(['wget2', '-O', html_path, args.url])
obj = lxml.html.parse(str(html_path))
game_table, = obj.xpath('//*[@id="games"]//tbody')

with sqlite3.connect(db_path) as conn:
    def rating(s):
        return None if s == '-' else float(mystrip(s, suffix='%'))
    conn.execute('PRAGMA journal_mode = wal')
    conn.execute('DROP TABLE IF EXISTS games')
    conn.execute('CREATE TABLE games (id INTEGER PRIMARY KEY, name TEXT, rating REAL, time INTEGER, price INTEGER)')
    conn.executemany(
        'INSERT INTO games (id, name, rating, time, price) VALUES (:id, :name, :rating, :time, :price)',
        ({'id': mystrip(tr.xpath('.//td/a/@href')[-1], prefix='/app/', suffix='/'),
          'name': tr.xpath('.//td/a/text()')[-1],
          'rating': rating(tr.xpath('.//td/text()')[-1]),
          'time': tr.xpath('.//td/@data-sort')[-1],
          'price': tr.xpath('.//td/@data-sort')[-2]}
         for tr in game_table.xpath('./tr')))
    conn.execute("UPDATE games SET time = NULL WHERE time = -1")
    conn.execute("UPDATE games SET price = NULL WHERE price = -1")
    conn.execute("""
    CREATE VIEW IF NOT EXISTS stats AS
    SELECT printf('%.2f hours', sum(time / 60.0)) AS total_playtime,
           printf('%.2f hours', avg(time / 60.0)) AS average_playtime,
           printf('%i A$', sum(price / 100)) AS total_spent,  -- at today's prices
           printf('%.2f A$', avg(price / 100.0)) AS average_price,
           -- "Average price calculation only includes games that have a price"
           printf('%.2f A$', avg(CASE WHEN price >0 THEN price ELSE NULL END / 100.0)) AS steamdb_average_price,
           printf('%.2f A$/hour', sum(price / 100.0) / sum(time / 60.0)) AS price_per_hour,
           printf('%.2f A$/hour', avg((price / 100.0) / max(1.0, (time / 60.0)))) AS average_price_per_hour,
           -- "Average price calculation only includes games that have a price"
           printf('%.2f A$/hour', avg((CASE WHEN price >0 THEN price ELSE NULL END / 100.0) / max(1.0, (time / 60.0)))) AS steamdb_average_price_per_hour
    FROM games
    """)
pathlib.Path('stats.ini').write_bytes(
    subprocess.check_output(['sqlite3', '-line', db_path, 'SELECT * FROM stats']))
