# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:09:32 2016

@author: Dave Ho
"""

def circular(ar):
    for i in range(0, len(ar)):
        visited = []
        pos = i
        while True:
            if (pos not in visited):
                visited.append(pos)
            else:
                break
            if (len(visited)==len(ar)):
                return True
            pos = (pos+ar[pos])%len(ar)
    return False