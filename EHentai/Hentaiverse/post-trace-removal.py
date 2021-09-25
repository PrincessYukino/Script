#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : PythonScript
# @file: post-trace-removal.py.py
# @time: 2021/7/18 18:34
# @desc:
import re
import time
import requests
from bs4 import BeautifulSoup

ipb_md5_check = "aa57a35434ab128b88f41b7790b0186c"


def eh_auth():
    session = requests.Session()
    EHLOGINURL = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"
    EHCREDENTIALS = {
        "UserName": "Grandmasters",
        "PassWord": "Ethwaitforme2022",
        "CookieDate": 1
    }
    session.post(EHLOGINURL, data=EHCREDENTIALS)
    return session


def quick_edit(info):
    global session
    resp = session.post(url="https://forums.e-hentai.org", data={
        "md5check": ipb_md5_check,
        "t": info[1],
        "p": info[2],
        "act": "xmlout",
        "do": "post-edit-save",
        "post": f"Achieved{time.time()}",
        "std_used": 1,
    })
    print(info)


def full_edit():
    global session
    resp = session.post(url="https://forums.e-hentai.org/index.php?", data={
        "act": "Post",
        "s": "",
        "auth_key": "aa57a35434ab128b88f41b7790b0186c",
        "t": info[1],
        "p": info[2],
        "st": 104400,
        "post_key": "36fa24f96e276bf593c398b285be3e67",
        "md5check": ipb_md5_check,
        "Post": f"Achieved{time.time()}",

    })
    print(info)


UID = 4697311
# BaseUrl = f"https://forums.e-hentai.org/index.php?act=Search&CODE=getalluser&mid={UID}"
BaseUrl = "https://forums.e-hentai.org/index.php?act=Search&nav=au&CODE=show&searchid=5523a049e08330f3c4f28cf518d76cfa&search_in=posts&result_type=posts"

pattern = re.compile(r'(\d+)')

if __name__ == '__main__':
    # session = requests.Session()
    session = eh_auth()
    html = session.get(url=BaseUrl)
    html = BeautifulSoup(html.text, 'html.parser')
    message_all = html.find_all("a", class_="linkthru")
    print(message_all)
    for message in message_all:
        strd = str(message.get("href"))
        if "view=findpost" in strd:
            info = pattern.findall(strd)
            quick_edit(info[0])
        else:
            continue
# https://forums.e-hentai.org/index.php?act=post&do=edit_post&f=12&t=201268&p=5949341&st=104400
