# !/usr/bin/python
# -*- coding: utf-8 -*-

L = [[True,True, True,True,True,True,True,True,True,True],
     [True,False,False,True,True,True,True,False,True,True],
     [True,True,False,False,False,False,False,False,False,True],
     [True,True,True,True,True,True,False,True,False,True],
     [True,True,False,True,True,True,False,True,False,True],
     [True,True,False,False,False,True,False,True,False,True],
     [True,True,False,True,False,True,False,True,False,True],
     [True,True,False,True,False,False,False,True,False,True],
     [False,False,False,True,True,True,False,True,False,False],
     [True,True, True,True,True,True,True,True,True,True]]

def resolver(L,e):
    print e       
    type(L)
    type(e)
    n = len(L[0]) 
    m = len(L)    
    x = e[0]      
    y = e[1]      
    if y == n-1 or x == m-1:    
        return e[0]+1,e[1]+1 
    else:
        if L[x][y+1] == False: 
            e = [x,y+1]         
            return resolver(L,e) 
        elif L[x+1][y] == False: 
            e = [x+1,y]                
            return resolver(L,e)
        elif L[x-1][y] == False:
            e = [x-1,y]
            return resolver(L,e)
        elif L[x][y-1] == False:
            e = [x,y-1]
            return resolver(L,e)
        else:
            print "ya no puede avanzar"
            
type(L)
e = [1,0]           
r = resolver(L,e)
import numpy as np
print(np.matrix(L))

#########################################

def malla(M,c):
    type(M)
    n = len(M[0])       #numero de columnas
    m = len(M)          #numero de filas
    l = n*m            #numero de casillas
    x = c[0]           #fija coord x de inicio
    y = c[0]           #fija coord y de inicio
    for i in range(l):
        if y == n or x == m:    
            return e[1]+1,e[1]+1
        else:
            if L[x][y+1] == False: 
                e = [x,y+1]         
                return malla(L,e) 
            elif L[x+1][y] == False: 
                e = [x+1,y]                
                return malla(L,e)
            elif L[x-1][y] == False:
                e = [x-1,y]
                return malla(L,e)
            elif L[x][y-1] == False:
                e = [x,y-1]
                return malla(L,e)
            else:
                print "ya no puede avanzar"
