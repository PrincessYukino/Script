#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvMonsterAvatar
# @file: monsterdbattack.py
# @time: 2021/5/23 16:29
# @desc:
import requests, json

data = {
    "monsterId": 249759,
    "monsterClass": "Undead",
    "monsterName": "Fucking Tenboro",
    "plvl": 2250,
    "attack": "Crushing",
    "trainer": 0,
    "piercing": 0,
    "crushing": 0,
    "slashing": 0,
    "cold": 0,
    "wind": 0,
    "elec": 0,
    "fire": 0,
    "dark": 0,
    "holy": 0,
}
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}
r = requests.put(url='https://hvdata.lastmen.men/monsterdata/', headers=headers, data=json.dumps(data))
print(r.text)
