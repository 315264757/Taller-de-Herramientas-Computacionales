# !/usr/bin/python
# -*- coding: utf-8 -*-

L = [1,2,3,4,5,6,7,8,9]
R = [1,2,3,4,5,6,7,8,9]
M = [1,3,2,4,5,6,7,8,9]
N = [1,2,3,4,5,6,7,8]

def longi(a,b):
    for i in a:
        if len(a) == len(b) and a[i] == b[i]:
            return True
        else:
            return False
