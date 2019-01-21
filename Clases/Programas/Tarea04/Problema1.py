#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

#def mcd(a,b):
#    q=1
#    r = a-b*q
#    while b*q<a:
#        q = q+1
#        r = a-b*q
#        while r != 0:
#            a = b
#            b = r
#            r = a-b*q
#        return(b)
#    return(b)

#def mcd(a,b):
#    q=1
#    r = a-b*q
#    while r != 0:
#        a = b
#        b = r
#        r = a-b*q
#        while (b*q)<a:
#            q = q+1
#            r = a-b*q


    
#def MCD(a,b):
#    q=1
#    r = a-b*q
#    while b*q<a:
#        q = q+1
#        r = a-b*q
#        while r != 0:
#            a = b
#            b = r
#            r = a-b*q    
#        return(r)
#        return(b)
#        print r
#        print b
#    return(r)
#    return(b)
#    print r
#    print b

def macomu(a,b):
    r = a-b
    while r>b:
        a = r
        r = a-b
    while r != 0:
        a = b
        b = r
        r = a-b
    return(b)


    
