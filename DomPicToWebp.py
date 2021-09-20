#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: Green Sulley
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: domPicToWebp.py
# @time: 2021/8/4 下午4:11
# @desc: batch conversion of picture files to WEBP
import os

for root, folder, files in os.walk(''):
    for file in files:
        a = file.split('.', 1)
        if len(a) == 2:
            file_suffix = a[1].lower()  # 后缀
        else:
            continue
        if file_suffix == 'md':
            with open(f'{root}/{file}', 'r') as f:
                b = f.read()
            with open(f'{root}/{file}', 'w+') as f:
                for i in ['png', 'jpeg', 'jpg']:
                    print(file)
                    b = b.replace(i, 'webp')
                f.write(b)
