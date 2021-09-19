#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvHeadless
# @file: auth.py
# @time: 2021/6/7 16:44
# @desc:
import json
import time
import requests


config = json.load(open('config.json'))



def eh_auth():
    session = requests.Session()
    EHLOGINURL = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"
    EHCREDENTIALS = {
        "UserName": config['Account']['account'],
        "PassWord": config['Account']['password'],
        "CookieDate": 1
    }
    session.post(EHLOGINURL, data=EHCREDENTIALS)
    return session


def eh_auth_check(session):
    if session.cookies:
        for c in session.cookies:
            if (c.domain == '.e-hentai.org'
                and c.name == '__cfduid'
                and c.expires > time()):
                return True
    return False


def hv_login():
    hv_login_url = f"http://alt.hentaiverse.org/login?ipb_member_id={config['ipb_member_id']}&ipb_pass_hash={config['ipb_pass_hash']}"
    session = requests.Session()
    session.get(hv_login_url)
    return session


def hv_auth_check(session):
    if session.cookies:
        for c in session.cookies:
            if (c.domain == '.hentaiverse.org'
                and c.name == '__cfduid'
                and c.expires > time()):
                return True
    return False
