#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-
import math

#def velocidad_inicial(v0,teta):
#    v0x = v0*math.cos(teta)
#    v0y = v0*math.sin(teta)
#    return(v0x)
#    return(v0y)

def posicion(v0x,v0y,t):
    g = 9.81
    x = x0+v0x*t
    y = y0+v0y*t-1.0/2*g*t**2
    return(x)
    return(y)

def altura_maxima(v0y,t0):
    g = 9.81
    vy = v0y-g*t0
    while vy != 0:
        t0 += 0.5
        return(t0)
    
#la altura maxima que alcanza el proyectil la encontramos cuando la velocidad en el eje vertical es cero
#lo que se hizo fue usar la formula de la posicion y se tiene que ingresar un valor de velocidad y tiempo inicial    
