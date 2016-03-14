#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

img = Image.open('oxygen.png')
data = [img.getpixel((i, j)) for i in range(0, 609) for j in range(43, 53)]
print(data)

# 先选取印第45行的所有像素信息
row = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 7)]
res = "".join(row)
print(res)

res = "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
print(res)