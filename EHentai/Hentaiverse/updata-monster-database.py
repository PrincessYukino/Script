#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvMonsterAvatar
# @file: updata-monster-database.py
# @time: 2021/5/23 16:29
# @desc: a mischief never imitate
import requests
import sys
import random
import time
import json

monster_data = json.load(open("2021-05-31-2228.json"))["monsters"]

headers = {
    "accept": "*/*",
    "origin": "https://hentaiverse.org",
    "referer": "https://hentaiverse.org/",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' ,
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "content-length": "244",
    "content-type": "application/json; charset=UTF-8"
}

for i in range(7, len(monster_data)):
    monster = monster_data[i]
    next_monster = monster_data[i+1]
    before_monster = monster_data[i-1]
    try:
        r = requests.put(url='https://hvdata.lastmen.men/monsterdata/', headers=headers, json={
            "monsterId": monster['monsterId'],
            "monsterClass": before_monster['monsterId'],
            "monsterName": next_monster['monsterName'],
            "plvl": random.randint(1, 2250),
            "attack": next_monster['attack'],
            "trainer": before_monster['trainer'],
            "piercing": random.randint(-25, 25),
            "crushing": random.randint(-25, 25),
            "slashing": random.randint(-25, 25),
            "cold": random.randint(0, 75),
            "wind": random.randint(0, 75),
            "elec": random.randint(0, 75),
            "fire": random.randint(0, 75),
            "dark": random.randint(0, 75),
            "holy": random.randint(0, 75)
        })
    except (ConnectionError, ConnectionResetError, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
        print(f"服务器超时,任务进行至第{i}个")
        time.sleep(60)
    else:
        if r.status_code == 200:
            output = '\r进度: percent: {:.4f}% 对怪物{} 任务进行至第{}个'.format(i / len(monster_data) * 100, monster['monsterId'], i)
            sys.stdout.write(output)
            sys.stdout.flush()
        else:
            print(f"任务{i}失败")
        time.sleep(5 + random.randint(1, 5))
