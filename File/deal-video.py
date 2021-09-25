#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvFinanceLogs
# @file: deal-video.py
# @time: 2021/4/17 1:07
# @desc: Cosersets File Check

import os

correct_suffix_video = ['mp4', 'mov']
correct_suffix_image = ['bin', 'webp', 'gif', 'jpg', 'jpeg', 'heic']

# E.G. => ./AAA ['BBB'] []
# root => 本目录
# folder => 本目录下的文件夹
# files => 本目录下的文件
print("━━━━━━━━开始━━━━━━━━")
for root, folder, files in os.walk('../'):
    print(f'━━当前目录为{root}')
    move = False
    detected_video = []
    detected_image = []
    if files:
        print("━━━━━开始查询视频文件━━━━━")
        for file in files:
            file_name = file.split('.', 1)[0].lower()  # 文件名
            file_suffix = file.split('.', 1)[1].lower()  # 文件后缀
            if file_suffix in correct_suffix_video:
                print(f'┃━━检测到视频{file}')
                detected_video.append([file_name, file])
            else:
                move = True
        print("━━━━━━━查询完毕━━━━━━━")
    else:
        print('┃━文件夹空！')
    if detected_video:
        print("━━━━━━━开始移动━━━━━━━")
        if move:
            for video in detected_video:
                print(f'┃━━将视频从{root}/{video[1]}移动至{root}/视频/{video[1]}')
                if not os.path.exists(f"{root}/视频"):
                    os.mkdir(f"{root}/视频")
                os.rename(f"{root}/{video[1]}", f"{root}/视频/{video[1]}")
        print("━━━━━━━移动结束━━━━━━━")
    else:
        print('┃━未检测到视频')
print("━━━━━━━━结束━━━━━━━━")
