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
subprocess.check_call(['sqlite3', db_path, '-init', 'schema.sql'], stdin=subprocess.DEVNULL)

with sqlite3.connect(db_path) as conn:
    def rating(s):
        return None if s == '-' else float(mystrip(s, suffix='%'))
    def fix(s):
        return None if s == '-1' else int(s)
    conn.executemany(
        'INSERT INTO games (id, name, rating, time, price) VALUES (:id, :name, :rating, :time, :price)',
        ({'id': mystrip(*tr.xpath('./td[3]/a/@href'), prefix='/app/', suffix='/'),
          'name': tr.xpath('./td[3]/a/text()')[0],
          'rating': rating(*tr.xpath('./td[7]/text()')),
          'time': fix(*tr.xpath('./td[6]/@data-sort')),
          'price': fix(*tr.xpath('./td[5]/@data-sort'))}
         for tr in game_table.xpath('./tr')))

pathlib.Path('stats.ini').write_bytes(
    subprocess.check_output(['sqlite3', '-line', db_path, 'SELECT * FROM stats_text']))
pathlib.Path('what-game-next.csv').write_bytes(
    subprocess.check_output(['sqlite3', '-header', '-csv', db_path, 'SELECT * FROM what_game_next']))
pathlib.Path('what-game-next-nonfree.csv').write_bytes(  # skip the "free to play" games
    subprocess.check_output(['sqlite3', '-header', '-csv', db_path, 'SELECT * FROM what_game_next WHERE "$" >0']))
pathlib.Path('what-game-next-to-lower-my-KPI.csv').write_bytes(
    subprocess.check_output(['sqlite3', '-header', '-csv', db_path, 'SELECT * FROM what_game_next_to_lower_my_KPI']))
