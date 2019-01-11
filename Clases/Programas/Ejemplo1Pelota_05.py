# -*- coding: utf-8 -*-
v0 = 34
g = 9.81
t = 4.3
y = v0*t - 1.0/2*g*t**2
print 'La posicion de la pelota en el t=%E es %10.7f\n%f' % (t,y,t)
def posicion(t,v0):
    y = v0*t - 1.0/2*g*t**2
    return(y)
