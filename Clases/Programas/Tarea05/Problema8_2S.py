# !/usr/bin/python
# -*- coding: utf-8 -*-

from Problema8_2 import *

print 'Dadas las ecuaciones recursivas'
print 'xtx_t=x(t) \n yt=x(t) \n zt=z(t)=1-xt-yt'

print 'Ejemplo: h=0.01, x0=0.4165, y0=0.4261, n=1095, alpha=0.2411, beta=0.008'

h = input('Dada una h suficientemente pequeña que defina la frecuencia en la que representaremos los datos')
n = input('Numero de experimentos para representar un muestreo significativo')
alpha = input('Probabilidad de contagio por contacto con infectado')
beta = input('Probabilidad de removerse de la infección')

x,y,z,t = iteracion(h,x0,y0,n,alpha,beta)
print(x,y,z,t)

