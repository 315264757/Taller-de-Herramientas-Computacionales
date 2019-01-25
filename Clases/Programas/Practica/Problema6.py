# !/usr/bin/python
# -*- coding: utf-8 -*-
 
print 'n es el numero que deseamos aplicarle la funcion factorial y n0 es el anterior a el'
def fact(n0,n):
    if(n == 0):             #caso base 0! = 1
        n0 = 1
    else:
        n0 = fact(n0,n-1)   #recursion
        n0 = n0*n           #multiplica por el anterior
    return n0
