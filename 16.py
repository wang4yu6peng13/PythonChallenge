#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('mozart.gif')
w, h = im.size
magenta = 195
bars = []
for j in range(h):
    for i in range(w - 5):
        if im.getpixel((i, j)) == magenta and im.getpixel((i + 4, j)) == magenta:
            bars.append((i, j))
print(bars[:10])

for i in range(h):
    if bars[i][1] != i:
        print(i)

shift = Image.new(im.mode, (w * 2, h), 0)
shift.palette = im.palette
for j in range(h):
    for i in range(w):
        shift.putpixel((i + w - bars[j][0], j), im.getpixel((i, j)))

shift.save('shift.png')

shift2 = Image.new(im.mode, (w * 2, h), 0)
shift2.palette = im.palette
for j in range(h):
    for i in range(w):
        shift2.putpixel(((i + w - bars[j][0]) % w, j), im.getpixel((i, j)))

shift2.save('shift2.png')
