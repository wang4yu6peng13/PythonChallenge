#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

strip = Image.open("wire.png")
spiral = Image.new(strip.mode, (100, 100), 0)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, z = -1, 0, 0
for i in range(200):
    d = dirs[i % 4]
    for j in range(100 - (i + 1) // 2):
        x += d[0]
        y += d[1]
        spiral.putpixel((x, y), strip.getpixel((z, 0)))
        z += 1

spiral.save("spriral.png")
