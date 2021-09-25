#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : Script
# @file: qqmusic-songlist-to-walkman.py
# @time: 2021/9/20 17:48
# @desc:
import os
import json
import requests


def songlist_info(songlist_id):
    resp = requests.get(
        url=f"https://api.qq.jsososo.com/songlist?id={songlist_id}")
    return resp.json()


def songlist_json(path='test.json'):
    with open(path) as f:
        return json.load(f)


def form_m3u8(songlist_str, songlist_path: str, relative_path: str):
    output = "#EXTM3U\n"
    for song in songlist_str:
        for i in os.listdir(songlist_path):
            if song in i:
                format = i.split('.', 1)[1]
                if format != 'lrc':
                    output += f"#EXTINF:,\n{relative_path}/{song}.{format}\n"
    return output


def main():
    songlist_with_path = []
    songlist = songlist_json()["data"]["songlist"]
    for song in songlist:
        songlist_with_path.append(
            f"{song['songname']} - {song['singer'][0]['name']}")
    out = form_m3u8(songlist_with_path,
                    "/Volumes/Untitled/MUSIC/动漫/ACG动漫主题曲精选",
                    "动漫/ACG动漫主题曲精选")
    print(out)


main()
