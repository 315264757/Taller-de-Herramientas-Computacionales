# !/usr/bin/python
# -*- coding: utf-8 -*-
import math

#este es inciso a) que calcula la funcion con sus condiciones correspondientes
def H_eps(x):
    e = 0.01
    H = 1/2 + x/(2*e) + 1/(2*e)*math.sin((math.pi*x/e))
    if x < (-e):
        H = 0
    elif x > e:
        H = 1
    print H

def prueba_H_eps():
    e = 0.01
    print H_eps(-10)
    print H_eps(0)
    print H_eps(-e)
    print H_eps(0.001)
