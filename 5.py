#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

# 以二进制形式读取文件内容
data = pickle.load(open('banner.p', 'rb'))
for each in data:
    print(each)
for each in data:
    line = "".join([i[1] * i[0] for i in each])
    print(line)