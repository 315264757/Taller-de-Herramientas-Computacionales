# !/usr/bin/python
# -*- coding: utf-8 -*-

def resolver(L,e):
    print e       #imprime los pasos
    type(L)
    type(e)
    n = len(L[0]) #numero de columnas
    m = len(L)    #numero de filas
    x = e[0]      #fija coord x de inicio
    y = e[1]      #fija coord y de inicio
    if y == n-1 or x == m-1:    #Pregunta si ya estas en la salida salida
        return e[0]+1,e[1]+1 #Regresa la salida
    else:
        if L[x][y+1] == False: #Pregunta si puedes avanzar uno a la derecha
            e = [x,y+1]         #Cambia la posicion inicial nueva
            return resolver(L,e) #Llamado recursivo
        elif L[x+1][y] == False: #Pregunta si puedes avanzar uno abajo
            e = [x+1,y]                
            return resolver(L,e)
        else:
            print "ya no puede avanzar"
            
L = [[True,True, True,True],
     [False,False,False,True],
     [True,True,False,True]]    #define el laberinto
type(L)
e = [1,0]           
r = resolver(L,e)
import numpy as np
print(np.matrix(L))
