# !/usr/bin/python
# -*- coding: utf-8 -*-

import scipy as sc
import numpy as np

x0=0.4165
y0=0.4261
z0=1-x0-y0
h=0.01
n=1095
alpha=0.2411
beta=0.008

def iteracion(h,x0,y0,n,alpha,beta):
    for i in range(0,n):    
            x = append(x[i]-h*alpha*x[i]*y[i])
            y = append(y[i]+h*alpha*x[i]*y[i]-h*beta*y[i])
            z = append(1-x[i]-y[i])
    return x,y,z,t
