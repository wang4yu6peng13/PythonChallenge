#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('cave.jpg')
w, h = im.size
for i in range(w):
    for j in range(h):
        if (i + j) % 2 == 1:
            im.putpixel((i, j), 0)

im.save('cave2.png')
