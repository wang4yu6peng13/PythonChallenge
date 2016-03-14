#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class solution10(object):
    def countAndSay(self, n):
        string = "1"
        for i in range(0, n):
            string = self.onecount(string)
        return string

    def onecount(self, numstr):
        strres = ""
        i = 0
        while i < len(numstr):
            j = i + 1
            while j < len(numstr) and numstr[i] == numstr[j]:
                j += 1
            count = j - i
            strres += str(count) + str(numstr[i])
            i = j
        return strres

solution = solution10()
res = solution.countAndSay(30)
print(len(res))