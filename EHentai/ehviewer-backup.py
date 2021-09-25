#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : Script
# @file: ehviewer-backup.py
# @time: 2021/9/19 23:58
# @desc:
import sys, time, yaml
import sqlite3


def get_bjtime():
    tn = time.localtime(time.time())
    return f"{tn.tm_year}{tn.tm_mon}{tn.tm_mday}{tn.tm_hour}{tn.tm_min}"


db_path = None

if db_path is None:
    if sys.argv[1:]:
        db_path = sys.argv[1:][0]
    else:
        db_path = input("Enter your ehviewer datebase path:")

conn = sqlite3.connect(db_path)
c = conn.cursor()
cursor = c.execute(
    "SELECT GID,TOKEN,TITLE,TITLE_JPN,THUMB,CATEGORY,POSTED,UPLOADER,RATING from HISTORY")
output = {}
output["type"] = "ehv_history"
output["data"] = {}

for row in cursor:
    output["data"][row[0]] = {
        "token": row[1],
        "title": row[2],
        "title_jpn": row[3],
        "thumb": row[4],
        "category": row[5],
        "posted": row[6],
        "uploader": row[7],
        "rating": row[8]
    }
conn.close()

with open(f'ehv-history-{get_bjtime()}.yaml', 'w') as nf:
    yaml.dump(output, nf)
