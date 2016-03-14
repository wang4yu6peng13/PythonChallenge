#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import string
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

def my_solution(text):
    o = ""
    for each in text:
        if ord(each) >= ord('a') and ord(each) <= ord('z'):
            o += chr((ord(each) + 2 - ord('a')) % 26 + ord('a')) # 尝试理解该转换公式
        else:
            o += each
    print(o)

def std_solution(text):
    table = str.maketrans(
            string.ascii_lowercase,
            string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    print(str.translate(text, table))

std_solution(text)
std_solution("map")