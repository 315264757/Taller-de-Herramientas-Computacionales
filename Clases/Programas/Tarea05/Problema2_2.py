#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

def coox(v0x):
    Lx = []
    x0 = 0
    t = 0
    for i in range(60):
        while t != 60:
            t += 1
            x = x0+v0x*t
            Lx.append(x)
        return(Lx)

def cooy(v0y):
    Ly = []
    g = 9.81
    y0 = 0
    t = 0
    for i in range(60):
        while t != 60:
            t += 1
            y = y0+v0y*t-1.0/2*g*t**2
            Ly.append(y)
        return(Ly)



#def posicion(v0x,v0y,x0,y0):
#    Lx = []
#    Ly = []
#    t = 0
#    g = 9.81
#    for i in range(60):
#        while t != 60:
#            t += 1
#            x = x0+v0x*t
#            Lx.append(x)
#        return(Lx)
#        for i in range(60):
#            while t != 60:
#                t += 1
#                y = y0+v0y*t-1.0/2*g*t**2
#                Ly.append(y)
#            return(Ly)

    
#def posicion(v0x,v0y,x0,y0):
#    L = []
#    t = 0
#    while t != 60:
#        t += 1
#        g = 9.81
#        x = x0+v0x*t
#        L.append(x)
#        y = y0+v0y*t-1.0/2*g*t**2
#        L.append(y)
#        return(L)
    
