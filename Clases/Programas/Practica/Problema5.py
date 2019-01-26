# !/usr/bin/python
# -*- coding: utf-8 -*-

a = 10
b = 14
n = 1

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
    maya = [[A,B] for A,B in zip(X,Y)]
    global maya
    return maya

def funcion():
    L = []
    for i in range(len(maya)):
        x = maya[i][0]
        y = maya[i][1]
        f = x**2/25 - y**2/49
        L.append(f)
        print L
        
