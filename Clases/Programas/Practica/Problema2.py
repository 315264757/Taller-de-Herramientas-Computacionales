#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-

def sigma(k):
    if k > 1:
        return(k**2 + sigma(k-1))
    else:
        return(1)
