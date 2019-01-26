# !/usr/bin/python
# -*- coding: utf-8 -*-


def malla(a,b,n):
    X = []
    x = 0
    y = 0
    for i in range(0,a,n):
        x += 0.5
        X.append(x)
    Y= []
    for i in range(0,b,n):
        y += 0.7
        Y.append(y)
    for A,B in zip(X,Y):
        print '%5.1f %5.1f' % (A,B)
