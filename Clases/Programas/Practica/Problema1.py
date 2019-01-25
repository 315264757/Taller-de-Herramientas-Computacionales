# !/usr/bin/python
# -*- coding: utf-8 -*-

def listC(x0,x1,n):
    gC = []
    dC = (x1 - x0)/float(n-1)
    for i in range(n):
        C = x0 + i*dC
        gC.append(C)
    return gC
