#!/usr/bin/python3
import argparse
import datetime
import pathlib
import random
import sqlite3
import subprocess

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
if False:
    # This is now a 403. --twb, June 2024
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
else:
    # Instead try browsing to it with Firefox then opening the saved file...
    # 1. Browse to https://steamdb.info/calculator/76561198815748328/?cc=au&all_games
    # 2. Save As
    # 3. Change format from "Web Page, complete" to "Web Page, HTML only".
    parser.add_argument(
        'html_path',
        nargs='?',
        default=pathlib.Path('~/Downloads/Trent W. Buck · Steam Calculator · 76561198815748328 · SteamDB.html').expanduser())
    args = parser.parse_args()
    html_path = args.html_path
    db_path = pathlib.Path('all-games.db')


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
        ({'id': mystrip(*tr.xpath('./td[3]/a/@href'),
                        # If you see 'https://steamdb.info/app/' prefix, you did
                        # Format: "Web Page, complete" not "Web Page, HTML only".
                        prefix='/app/' if True else 'https://steamdb.info/app/',  # changed in saved-from-Firefox version
                        suffix='/'),
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


print(' == Random selection of paid games weighted rating by rating/hour... == ')
print(*random.choices(*zip(*conn.execute('SELECT name, CAST("rating/hour" AS REAL) FROM what_game_next WHERE "$" >0').fetchall()), k=100), sep='\n')
