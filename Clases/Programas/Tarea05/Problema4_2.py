#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

def fibo(n):
    if n<2:
        return(n)
    else:
        return(fibo(n-1)+fibo(n-2))

