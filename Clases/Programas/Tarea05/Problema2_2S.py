#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-
from Problema2_2 import *

x = input("Ingresa el valor de velocidad inicial horizontal")
y = input("Ingresa el valor de velocidad inicial vertical")

mrux = coox(x)
mruay = cooy(y)

coord = [[C,F] for C,F in zip(mrux,mruay)]
print "las coordenadas del proyectil durante 60 segundos del tiro parabòlico oblicuo son:"
print(coord)

