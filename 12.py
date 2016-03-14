#!/usr/bin/env python3
# -*- coding: utf-8 -*-

gfx = open('evil2.gfx','rb').read()
types = ['jpg','png','gif','png','jpg']
for i in range(5): 
    open('evil2%d.%s' % (i, types[i]),'wb').write(gfx[i::5])