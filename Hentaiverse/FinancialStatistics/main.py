#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : FinancialStatistics
# @file: main.py
# @time: 2021/6/7 16:32
# @desc:

import requests

ipb_member_id = ''
ipb_pass_hash = ''

session = requests.Session()
if ipb_member_id and ipb_pass_hash:
    session.get(f'http://alt.hentaiverse.org/login?ipb_member_id={ipb_member_id}&ipb_pass_hash={ipb_pass_hash}')
else:
    exit()


