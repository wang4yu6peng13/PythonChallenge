#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

for year in range(1996, 1582, -20):
    if datetime.date(year, 1, 1).weekday() == 3:  # Thursday
        print(year)

# it’s Mozart’s birthday