#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

def mayomeno(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    L = []
    a = n1
    b = n2
    c = n3
    d = n4
    e = n5
    f = n6
    g = n7
    h = n8
    i = n9
    j = n10
    if a<b and a<c and a<d and a<e and a<f and a<g and a<h and a<i and a<j:
        menor = a
    elif b<a and b<c and b<d and b<e and b<f and b<g and b<h and b<i and b<j:
        menor = b
    elif c<a and c<b and c<d and c<e and c<f and c<g and c<h and c<i and c<j:
        menor = c
    elif d<a and d<c and d<b and d<e and d<f and d<g and d<h and d<i and d<j:
        menor = d
    elif e<b and e<c and e<d and e<a and e<f and e<g and e<h and e<i and e<j:
        menor = e
    elif f<b and f<c and f<d and f<e and f<a and f<g and f<h and f<i and f<j:
        menor = f
    elif g<b and g<c and g<d and g<e and g<f and g<a and g<h and g<i and g<j:
        menor = g
    elif h<b and h<c and h<d and h<e and h<f and h<g and h<a and h<i and h<j:
        menor = h
    elif i<b and i<c and i<d and i<e and i<f and i<g and i<h and i<a and i<j:
        menor = i
    elif j<b and j<c and j<d and j<e and j<f and j<g and j<h and j<i and j<a:
        menor = j
    else:
        print 'No hay numero menor'
    if a>b and a>c and a>d and a>e and a>f and a>g and a>h and a>i and a>j:
        mayor = a
    elif b>a and b>c and b>d and b>e and b>f and b>g and b>h and b>i and b>j:
        mayor = b
    elif c>a and c>b and c>d and c>e and c>f and c>g and c>h and c>i and c>j:
        mayor = c
    elif d>a and d>c and d>b and d>e and d>f and d>g and d>h and d>i and d>j:
        mayor = d
    elif e>b and e>c and e>d and e>a and e>f and e>g and e>h and e>i and e>j:
        mayor = e
    elif f>b and f>c and f>d and f>e and f>a and f>g and f>h and f>i and f>j:
        mayor = f
    elif g>b and g>c and g>d and g>e and g>f and g>a and g>h and g>i and g>j:
        mayor = g
    elif h>b and h>c and h>d and h>e and h>f and h>g and h>a and h>i and h>j:
        mayor = h
    elif i>b and i>c and i>d and i>e and i>f and i>g and i>h and i>a and i>j:
        mayor = i
    elif j>b and j>c and j>d and j>e and j>f and j>g and j>h and j>i and j>a:
        mayor = j
    else:
        print 'No hay numero mayor'
    L.append(menor)
    L.append(mayor)
    return L
    
