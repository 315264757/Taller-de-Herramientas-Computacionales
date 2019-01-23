#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

def mcd(a,b):
    L = []
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return(b)

def mcd(a,b):
    L = []
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
        L.append(b)
    return(L)

