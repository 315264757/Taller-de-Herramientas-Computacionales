# !/usr/bin/python
# -*- coding: utf-8 -*-

x0 = 10
x1 = 20
n = 3

def lC(x0,x1,n):
    gC = []
    dC = (x1 - x0)/float(n-1)
    for i in range(n):
        C = x0 + i*dC
        gC.append(C)
    return gC

def lA():
    gA = []
    for i in range(x0,x1-1,n):
        C = -20 + i*2.5
        gA.append(C)
    return gA

def lF(gC):
    gF = []
    for C in gC:
        F = (9.0/5)* C + 32
        gF.append(F)
    return gF

a = lC(x0,x1,n)
b = lF(a)
c = lA()

def lD():
    gD = []
    for i in range(len(a)):
        gd = a[i]-c[i]
        gD.append(gd)
    return gD

d = lD()

def showL(gF,gC,gA,gD):
    for F,C,A,D in zip(gF,gC,gA,gD):
        print '%8d %8d %8d %8d' % (C,F,A,D)

Problema1 = showL(a,b,c,d)
print Problema1
