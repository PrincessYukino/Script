#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : FinancialStatistics
# @file: visual.py
# @time: 2021/6/7 16:45
# @desc:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2.3, 3.4, 1.2, 6.6, 7.0]
plt.scatter(x, y, color='r', marker='+')
plt.show()
