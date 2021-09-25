#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : Script
# @file: get-qqmusic-songlist.py
# @time: 2021/9/20 17:48
# @desc:
import json
import requests


def songlist_info(songlist_id):
    resp = requests.get(
        url=f"https://api.qq.jsososo.com/songlist?id={songlist_id}")
    return resp.json()


def songlist_json(path='test.json'):
    with open(path) as f:
        return json.load(f)


def main():
    songlist_with_path = []
    songlist = songlist_json()["data"]["songlist"]
    for song in songlist:
        songlist_with_path.append(
            f"{song['songname']} - {song['singer'][0]['name']}")
    print(songlist_with_path)


main()
