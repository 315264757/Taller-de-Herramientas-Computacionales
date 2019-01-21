#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-
from Problema1 import mcd
a = input("Ingresa el primer número")
b = input("Ingresa el segundo número")
print "El máximo común divisor de %d y %d es %d" % (a,b,mcd(a,b))
