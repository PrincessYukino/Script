#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : FinancialStatistics
# @file: formdata.py
# @time: 2021/6/7 16:47
# @desc:
import auth
import requests
from bs4 import BeautifulSoup as Soup


session = auth.hv_login()


