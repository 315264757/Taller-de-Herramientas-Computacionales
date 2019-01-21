#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

from Problema2 import altura_maxima as amax
a = input ("Ingresa el valor de velocidad inicial vertical")
b = input ("Ingresa el valor de el tiempo inicial")
print "El proyectil con tiempo inicial %g tardó %f segundos en alcanzar su altura máxima" % (b,amax(a,b))
