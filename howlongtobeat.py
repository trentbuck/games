import json
import random
import sqlite3
import logging

import httpx

logging.basicConfig(level=logging.INFO)
sess = httpx.Client(http2=True)
sess.headers.update(
    headers={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'referer': 'https://howlongtobeat.com/'})


with sqlite3.connect('all-games.db') as conn:
    rows = conn.execute(
        """
        SELECT games.name FROM games
        LEFT OUTER JOIN howlongtobeat ON (games.id = howlongtobeat.profile_steam)
        WHERE howlongtobeat.profile_steam IS NULL  -- haven't already fetched it
        AND price                                  -- skip free-to-play games initially
        ORDER BY time DESC                         -- initially sort by play time
        """).fetchall()
    # random.shuffle(rows)
    for game_name, in rows:
        logging.debug('QUERY %s', game_name)
        resp = sess.post('https://howlongtobeat.com/api/search',
                         json={"useCache": True,
                               # If there's e.g. Final Fantasy VII for both PS1 and PC,
                               # skip the former.
                               "searchOptions": {"platform": "PC"},
                               # NOTE: may want to use "searchTerms": game_name.split(), e.g.
                               # INFO:root:RESULTS My Time at Portia 1
                               # INFO:root:RESULTS STAR WARS™ Jedi Knight: Jedi Academy™ 0   <---
                               # INFO:root:RESULTS UFO: Aftershock 1
                               # INFO:root:RESULTS You Suck at Parking® - Complete Edition 0 <---
                               # "searchTerms": [game_name],
                               "searchTerms": (
                                   game_name
                                   .replace('®', '')
                                   .replace('™', '')
                                   .split()),
                               })
        resp.raise_for_status()
        logging.info('RESULTS %s %s', game_name, len(resp.json()['data']))
        conn.executemany(
            """
            INSERT INTO howlongtobeat (game_id, game_name, profile_steam, comp_main, comp_plus, comp_100, comp_all)
            VALUES (:game_id, :game_name, :profile_steam, :comp_main, :comp_plus, :comp_100, :comp_all)
            ON CONFLICT DO NOTHING;
            """,
            resp.json()['data'])
        conn.commit()


example_reponse = {
    "color": "blue",
    "title": "",
    "category": "games",
    "count": 1,
    "pageCurrent": 1,
    "pageTotal": 1,
    "pageSize": 20,
    "data": [
        {
            "game_id": 87336,
            "game_name": "BEAR, VODKA, STALINGRAD!",
            "game_name_date": 0,
            "game_alias": "",
            "game_type": "game",
            "game_image": "87336_BEAR_VODKA_STALINGRAD.jpg",
            "comp_lvl_combine": 0,
            "comp_lvl_sp": 1,
            "comp_lvl_co": 0,
            "comp_lvl_mp": 0,
            "comp_lvl_spd": 1,
            "comp_main": 75,
            "comp_plus": 0,
            "comp_100": 225,
            "comp_all": 153,
            "comp_main_count": 2,
            "comp_plus_count": 0,
            "comp_100_count": 4,
            "comp_all_count": 6,
            "invested_co": 0,
            "invested_mp": 0,
            "invested_co_count": 0,
            "invested_mp_count": 0,
            "count_comp": 26,
            "count_speedrun": 0,
            "count_backlog": 18,
            "count_review": 5,
            "review_score": 25,
            "count_playing": 0,
            "count_retired": 5,
            "profile_dev": "Rabotiagi games",
            "profile_popular": 12,
            "profile_steam": 1232130,
            "profile_platform": "PC",
            "release_world": 2020
        }
    ],
    "userData": [],
    "displayModifier": None
}
