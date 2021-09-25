#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : Script
# @file: recode-lrc.py
# @time: 2021/9/20 17:48
# @desc: fix .lrc format problem causing Walkman ZX300A to display garbled characters

import os
import codecs

count = 0

for root, folder, files in os.walk(r'L:\MUSIC'):
    if files:
        for file in files:
            file_name = file.split('.', 1)[0]  # =>文件名=>名称
            file_suffix = file.split('.', 1)[1].lower()  # 后缀
            if file_suffix == "lrc":
                count += 1
                try:
                    with codecs.open(f'{root}/{file}', 'r',
                                     encoding='utf_8_sig') as f:
                        a = f.read()
                except UnicodeError:
                    with codecs.open(f'{root}/{file}', 'r',
                                     encoding='gbk') as f:
                        a = f.read()

                with codecs.open(f'{root}/{file}', 'w',
                                 encoding='utf_8_sig') as f:
                    f.write(a)
            else:
                continue

print(f"Success recode {count} lrc files")
