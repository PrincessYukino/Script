#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : FinancialStatistics
# @file: check-owner.py
# @time: 2021/6/7 19:23
# @desc:
import re
import auth
import requests
from bs4 import BeautifulSoup as Soup


def check(url):
    global session
    resp = session.get(url=url)
    resp = Soup(resp.text, 'html.parser')
    if "No such item" in resp.text:
        return 1
    owner = resp.find("a", {"target": "_forums"})
    if owner:
        return owner.text


if __name__ == '__main__':
    session = auth.hv_login()
    a = 0
    for i in all:
        a += 1
        owner = check(i)
        if owner == 1:
            print(f"装备被洗:{i}")
        if owner != "":
            print(f"拥有者错误:{i}")
