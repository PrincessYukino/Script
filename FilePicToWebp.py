from PIL import Image
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: Green Sulley
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: filePicToWebp.py
# @time: 2021/8/3 下午8:30
# @desc:
from PIL import Image
import os

IF_DELETE_OR = True
IGNORE_FILE = ['.npmignore', '.DS_Store', '.gitignore', 'package.json', '.gitattributes']
IGNORE_FOLDER = ['.git']
REPLACE_FILE = ['jpeg', 'jpg', 'png']


def pic_webp(picpath):
    image_path = picpath.split(".")[0]
    output_path = image_path + ".webp"
    im = Image.open(picpath)
    im.save(output_path)
    if IF_DELETE_OR:
        os.remove(picpath)


if __name__ == '__main__':
    for root, folder, files in os.walk(''):
        if os.path.basename(root) == ".git":
            folder[:] = []
            continue
        if files:
            for file in files:
                if file in IGNORE_FILE:
                    continue
                file_name = file.split('.', 1)[0]  # =>文件名=>名称
                file_suffix = file.split('.', 1)[1].lower()  # 后缀
                if file_suffix in REPLACE_FILE:
                    pic_webp(f'{root}/{file}')
                else:
                    continue
