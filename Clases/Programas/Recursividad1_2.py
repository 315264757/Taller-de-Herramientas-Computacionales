# !/usr/bin/python
# -*- coding: utf-8 -*-

def printr(L):
    if len(L) != 1:
        #print(L[1:] + L[:1])  ERROR
        print(L[0]) #si aqui pusiera coma la lista la da horizontal
        printr(L[1:])
    else:
        print(L[:1])

def printx(L):
    if L:
        print L[0],
        printx(L[1:])
    else:
        None

def printy(L):
    if len(L)>1:
        print(L[0]),
        printy(L[1:])
    else:
        print(L[0])
        



    #print L[:1]
    #print L[1:]
    #print(r)
