#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
text = open('character.txt').read()
res = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))
print(res)