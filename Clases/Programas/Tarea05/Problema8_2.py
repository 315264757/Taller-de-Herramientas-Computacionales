# !/usr/bin/python
# -*- coding: utf-8 -*-

import scipy as sc
import numpy as np
# Dadas las ecuaciones
#xtx_t=x(t)
#yt=x(t)
#zt=z(t)=1-xt-yt


#codigo para calcular el indice de infección por suceptibles removidos e infectados

#Tenemos las condiciones inciales
x0=0.4165
y0=0.4261
z0=1-x0-y0
#Definimos parametros
#h=0.01     #Dada h suficientemente pequeña
#n=1095    #Experimentos para representar un muestreo significativo
#alpha=0.2411   #Probabilidad de contgio a partir del contacto con el servidor infectado
#beta=0.008    #Probabilidad de ser removido

#Creamos listas y agregamos valores iniciales en la iteracion
def iteracion(h,x0,y0,n,alpha,beta):
    x=[]
    y=[]
    z=[]
    t=[]
    x.append(x0)
    y.append(y0)
    z.append(z0)
    t.append(0.0)
    for i in range(0,n):    #Que cumplen para tiempos discretos que n--->t0+nh
            x.append(x[i]-h*alpha*x[i]*y[i])
            y.append(y[i]+h*alpha*x[i]*y[i]-h*beta*y[i])
            z.append(1-x[i]-y[i])
    return x,y,z,t

#Llamamos a la función que creamos previamente de iteración
#x,y,z,t=iteracion(h,x0,y0,n,alpha,beta)    
#print(x,y,z,t)
