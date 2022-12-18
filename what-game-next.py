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

# Gives better error reporting than conn.executescript(schema_path.read_text()).
subprocess.check_call(['sqlite3', db_path, '-init', 'schema.sql'])

with sqlite3.connect(db_path) as conn:
    def rating(s):
        return None if s == '-' else float(mystrip(s, suffix='%'))
    def fix(s):
        return None if s == '-1' else int(s)
    conn.executemany(
        'INSERT INTO games (id, name, rating, time, price) VALUES (:id, :name, :rating, :time, :price)',
        ({'id': mystrip(tr.xpath('.//td/a/@href')[-1], prefix='/app/', suffix='/'),
          'name': tr.xpath('.//td/a/text()')[-1],
          'rating': rating(tr.xpath('.//td/text()')[-1]),
          'time': fix(tr.xpath('.//td/@data-sort')[-1]),
          'price': fix(tr.xpath('.//td/@data-sort')[-2])}
         for tr in game_table.xpath('./tr')))

pathlib.Path('stats.ini').write_bytes(
    subprocess.check_output(['sqlite3', '-line', db_path, 'SELECT * FROM stats_text']))
pathlib.Path('what-game-next.tsv').write_bytes(
    subprocess.check_output(['sqlite3', '-header', '-tabs', db_path, 'SELECT * FROM what_game_next ORDER BY price_per_hour_change_after_1h_more_play DESC ']))
pathlib.Path('what-game-next-to-lower-my-KPI.tsv').write_bytes(
    subprocess.check_output(['sqlite3', '-header', '-tabs', db_path, 'SELECT * FROM what_game_next_to_lower_my_KPI']))
