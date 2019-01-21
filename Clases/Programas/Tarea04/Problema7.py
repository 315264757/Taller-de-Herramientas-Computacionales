#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

def menor(a,b,c,d,e,f,g,h,i,j):
    if a<b<c<d<e<f<g<h<i<j:
        print "El numero menor es %d" % (a)
    elif b<a<c<d<e<f<g<h<i<j:
        print "El numero menor es %d" % (b)
    elif c<a<b<d<e<f<g<h<i<j:
        print "El numero menor es %d" % (c)
    elif d<a<b<c<e<f<g<h<i<j:
        print "El numero menor es %d" % (d)
    elif e<a<b<c<d<f<g<h<i<j:
        print "El numero menor es %d" % (e)
    elif f<a<b<c<d<e<g<h<i<j:
        print "El numero menor es %d" % (f)
    elif g<a<b<c<d<e<f<h<i<j:
        print "El numero menor es %d" % (g)
    elif h<a<b<c<d<e<f<g<i<j:
        print "El numero menor es %d" % (h)
    elif i<a<b<c<d<e<f<g<h<j:
        print "El numero menor es %d" % (i)
    elif j<a<b<c<d<e<f<g<h<i:
        print "El numero menor es %d" % (j)
    else:
        print "No hay numero menor o hay más de uno"

def mayor(a,b,c,d,e,f,g,h,i,j):
    if a>b>c>d>e>f>g>h>i>j:
        print "El numero mayor es %d" % (a)
    elif b>a>c>d>e>f>g>h>i>j:
        print "El numero mayor es %d" % (b)
    elif c>a>b>d>e>f>g>h>i>j:
        print "El numero mayor es %d" % (c)
    elif d>a>b>c>e>f>g>h>i>j:
        print "El numero mayor es %d" % (d)
    elif e>a>b>c>d>f>g>h>i>j:
        print "El numero mayor es %d" % (e)
    elif f>a>b>c>d>e>g>h>i>j:
        print "El numero mayor es %d" % (f)
    elif g>a>b>c>d>e>f>h>i<j:
        print "El numero mayor es %d" % (g)
    elif h>a>b>c>d>e>f>g>i>j:
        print "El numero mayor es %d" % (h)
    elif i>a>b>c>d>e>f>g>h>j:
        print "El numero mayor es %d" % (i)
    elif j>a>b>c>d>e>f>g>h>i:
        print "El numero mayor es %d" % (j)
    else:
        print "No hay numero mayor o hay más de uno"
