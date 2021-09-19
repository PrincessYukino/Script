#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvHeadless
# @file: testing.py
# @time: 2021/6/1 22:43
# @desc:
import json

monster_data = json.load(open("2021-05-31-2228.json"))
print(monster_data["monsters"][0])
