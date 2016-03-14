#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = ''.join([line.rstrip() for line in open('mess.txt')])
occ = {}

for c in s:
    occ[c] = occ.get(c, 0) + 1  # 相同的字符，字典的值加1
    avgOC = len(s) // len(occ)

print(''.join([c for c in s if occ[c] < avgOC]))