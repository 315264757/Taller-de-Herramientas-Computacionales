# !/usr/bin/python
# -*- coding: utf-8 -*-

n = input("¿cuantos valores?")
L=[]
for i in range(n):
    valor = input("Dame el valor")
    L.append(valor)

M=range(n)
for i in M:
    valor = input("Dame el valor")
    M[i](valor)

N=range(n)
j=0
while j<n:
    valor = input("Dame el valor")
    N[i](valor)

L=range
print "La lista es de tamano %d" % (len(L))
print L

OtraLista = input("")
