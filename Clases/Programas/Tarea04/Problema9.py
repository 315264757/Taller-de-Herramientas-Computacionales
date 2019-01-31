# !/usr/bin/python
# -*- coding: utf-8 -*-

import math

#este codigo sirve para saber de cuantas  maneras se puede rrearreglar un numero de telefon
#el numero debe dconstar de ocho digitos

def rearreglo(p1,p2,p3,p4,p5,p6,p7,p8):
    p = math.factorial(8)
    if p1 != p2 and p1 != p3 and p1 != p4 and \
    p1 != p5 and p1 != p6 and p1 != p7 and p1 != p8 and p2 != p3 and \
    p2 != p4 and p2 != p5 and p2 != p6 and p2 != p7 and p2 != p8 and \
    p3 != p4 and p3 != p5 and p3 != p6 and p3 != p7 and p3 != p8 and \
    p4 != p5 and p4 != p6 and p4 != p7 and p4 != p8 and \
    p5 != p6 and p5 != p7 and p5 != p8 and \
    p6 != p7 and p6 != p8 and \
    p7 != p8:
        q = 1
    elif p1 == p2 or p1 == p3 or p1 == p4 or \
    p1 == p5 or p1 == p6 or p1 == p7 or p1 == p8 or p2 == p3 or \
    p2 == p4 or p2 == p5 or p2 == p6 or p2 == p7 or p2 == p8 or \
    p3 == p4 or p3 == p5 or p3 == p6 or p3 == p7 or p3 == p8 or \
    p4 == p5 or p4 == p6 or p4 == p7 or p4 == p8 or \
    p5 == p6 or p5 == p7 or p5 == p8 or \
    p6 == p7 or p6 == p8 or \
    p7 == p8:
        q = math.factorial(2)
    #elif p1 == p2 and p1 == p3 and p1 == p4 and \
    #p1 == p5 and p1 == p6 and p1 == p7 and p1 == p8 and p2 == p3 and \
    #p2 == p4 and p2 == p5 and p2 == p6 and p2 == p7 and p2 == p8 and \
    #p3 == p4 and p3 == p5 and p3 == p6 and p3 == p7 and p3 == p8 and \
    #p4 == p5 and p4 == p6 and p4 == p7 and p4 == p8 and \
    #p5 == p6 and p5 == p7 and p5 == p8 and \
    #p6 == p7 and p6 == p8 and \
    #p7 == p8:
    elif p1 == p2 and p2 == p3 and p3 == p4 and p4 == p5 \
         and p5 == p6 and p6 == p7 and p7 == p8:
        q = math.factorial(8)
    else:
        None
    return q
        
        
        
    
    
    
