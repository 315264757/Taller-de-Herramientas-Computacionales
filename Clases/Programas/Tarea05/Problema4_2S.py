#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-
from Problema4_2 import *

n = input("Ingresa hasta que numero de la sucesion deseas calcular")
#ene = fibo(n) 

#print(ene)

L = []
for i in range(n):
    ene = fibo(i)
    L.append(ene)
    print(L)
