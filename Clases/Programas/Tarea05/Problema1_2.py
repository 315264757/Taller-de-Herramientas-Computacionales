# !/usr/bin/python
# -*- coding: utf-8 -*-

def mcd(a,b):
    L = []
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return(b)

def pasos(a,b):
    L = []
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
        L.append(b)
    return(L)

#def macomu(a,b):
#    r = a-b
#    #for i in b
#    while r>b:
#        a = r
#        r = a-b
#    while r != 0:
#        a = b
#        b = r
#        r = a-b
#    return(b)

#def residuo(a,b):
#    L = []
#    r = a-b
#    L.append(r)
#    while r>b:
#        a = r
#        r = a-b
#        L.append(r)
#    while r != 0:
#        a = b
#        b = r
#        r = a-b
#        L.append(r)
#    return(L)
