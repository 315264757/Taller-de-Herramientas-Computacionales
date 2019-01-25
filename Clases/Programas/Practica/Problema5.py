# !/usr/bin/python
# -*- coding: utf-8 -*-


def malla(a,b,n):
    X = []
    for i in range(0,a,n):
        x = a
        X.append(x)
    Y= []
    for i in range(0,b,n):
        y = b
        Y.append(y)
    for A,B in zip(X,Y):
        print '%5.1f %5.1f' % (A,B)
