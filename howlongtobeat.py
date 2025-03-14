import json
import json
import logging
import lxml.html
import random
import re
import sqlite3
import sys

import httpx

logging.basicConfig(level=logging.INFO)
sess = httpx.Client(http2=True)
sess.headers.update(
    headers={
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'referer': 'https://howlongtobeat.com/'})


# As at October 2024, this is now gone...
# I can see it at curl https://howlongtobeat.com/game/93960 | grep -Fw 1599020
# "profile_steam": 1232130,
def fudge_json(j: dict) -> dict:
    if 'profile_steam' in j:
        return j
    url = f"https://howlongtobeat.com/game/{j['game_id']}"
    resp = sess.get(url)
    resp.raise_for_status()
    obj = lxml.html.fromstring(resp.content)  # BYTES
    new_str, = obj.xpath('//script[@id="__NEXT_DATA__"]/text()')
    new_dict = json.loads(new_str)
    profile_steam = max(
        game_dict['profile_steam']
        for game_dict in new_dict['props']['pageProps']['game']['data']['game'])
    j['profile_steam'] = profile_steam
    # I think returning a partial record might be how they're treating anyone they think is scraping now???
    # if not(any(k in j for k in {'comp_main', 'comp_all', 'comp_100', 'comp_plus'})):
    #     logging.warning('SKIPPING! %s (%s)', j['game_name'], j['profile_steam'])
    #     return {'comp_main': None, 'comp_all': None, 'comp_100': None, 'comp_plus': None} | j
    logging.info('profile_steam %s', profile_steam)
    return j


with sqlite3.connect('all-games.db') as conn:
    rows = conn.execute(
        """
        -- SELECT games.name FROM games
        -- LEFT OUTER JOIN howlongtobeat ON (games.id = howlongtobeat.profile_steam)
        -- WHERE howlongtobeat.profile_steam IS NULL  -- haven't already fetched it
        -- AND price                                  -- skip free-to-play games
        -- -- ORDER BY time desc
        -- ORDER BY rating desc
        SELECT name FROM what_game_next WHERE hltb IS NULL AND "$" IS NOT NULL
        """).fetchall()
    # random.shuffle(rows)
    game_names = sys.argv[1:] or [cell for cell, in rows]
    for game_name in game_names:
        logging.debug('QUERY %s', game_name)
        resp = sess.post('https://howlongtobeat.com/api/ouch/0980d1750bf5c22b',
                         json={
                             "searchType":"games",
                             "searchTerms": (
                                 game_name
                                 .replace('®', '')
                                 .replace('™', '')
                                 .split()),
                             "searchPage":1,
                             "size":20,
                             "searchOptions":{"games":{"userId":0,
                                                       "platform":"",
                                                       "sortCategory":"popular",
                                                       "rangeCategory":"main",
                                                       "rangeTime":{"min": None,
                                                                    "max": None},
                                                       "gameplay":{"perspective":"",
                                                                   "flow":"",
                                                                   "genre":"",
                                                                   "difficulty":""},
                                                       "rangeYear":{"min":"",
                                                                    "max":""},
                                                       "modifier":""},
                                              "users":{"sortCategory":"postcount"},
                                              "lists":{"sortCategory":"follows"},
                                              "filter":"",
                                              "sort":0,
                                              "randomizer":0},
                             "useCache":True}
                         )
        resp.raise_for_status()
        logging.info('RESULTS %s %s', game_name, len(resp.json()['data']))
        conn.executemany(
            """
            INSERT INTO howlongtobeat (game_id, game_name, profile_steam, comp_main, comp_plus, comp_100, comp_all)
            VALUES (:game_id, :game_name, :profile_steam, :comp_main, :comp_plus, :comp_100, :comp_all)
            ON CONFLICT DO NOTHING;
            """,
            map(fudge_json, resp.json()['data']))
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
# As at October 2024, this is now gone...
# I can see it at curl https://howlongtobeat.com/game/93960 | grep -Fw 1599020
            "profile_steam": 1232130,
            "profile_platform": "PC",
            "release_world": 2020
        }
    ],
    "userData": [],
    "displayModifier": None
}
