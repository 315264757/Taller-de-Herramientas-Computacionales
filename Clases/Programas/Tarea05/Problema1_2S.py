# !/usr/bin/python
# -*- coding: utf-8 -*-
from Problema1_2 import *

a = input("Ingresa el numero mayor")
b = input("Ingresa el numero menor")

print 'El máximo común divisor de %d y de %d es %d' % (a,b,mcd(a,b))
print 'Los residuos en cada paso andtes de ser cero fueron:'
print(pasos(a,b))
