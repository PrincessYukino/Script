#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: GPL v3
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvMonsterAvatar
# @file: pid-to-author.py
# @time: 2021/5/23 16:52
# @desc: 根据文件名的PID移动至对应作者名称文件夹

import requests, os
import json, time
from bs4 import BeautifulSoup as Bs

suffix_image = ['jpg', 'webp', 'png', 'webm']


def get_author(pid):
    url = f'https://www.pixiv.net/artworks/{pid}'
    resp = session.get(url)
    resp = Bs(resp.text, 'html.parser')
    meta_info = resp.find(attrs={"name": "preload-data"})['content']
    uid = json.loads(meta_info)["illust"][str(pid)]["userName"]
    return uid


if __name__ == '__main__':
    session = requests.Session()

    for root, folder, files in os.walk('../'):
        time.sleep(1)
        print(f'━━当前目录为{root}')
        move = False
        detected_video = []
        detected_image = []
        if files:
            print("━━━━━开始搜索图片文件━━━━━")
            for file in files:
                file_name = file.split('.', 1)[0]  # =>文件名=>pid)
                if "_" in file:
                    file_name = file_name.split('_', 1)[0]
                if not file_name.isdigit():
                    print(f"┃━{file}不是有效文件")
                    continue
                file_suffix = file.split('.', 1)[1].lower()  # 文件后缀
                if file_suffix in suffix_image:
                    print(f'┃━━检测到图片{file}')
                    pid = get_author(int(file_name))
                    if not os.path.exists(f"{root}/out/{pid}/"):
                        os.makedirs(f"{root}/out/{pid}/")
                    os.rename(f"{root}/{file}", f"{root}/out/{pid}/{file}")
                    print(f'   图片{file}移动到{pid}━━┃')
            print("━━━━━━━搜索完毕━━━━━━━")
        else:
            print('┃━文件夹空！')
