# !/usr/bin/python
# -*- coding: utf-8 -*-

#def generador():
#    for i in [1,2,3]:
#        yield i
#    for n in generador():
#        print(n) 

def lista_infinita():
    i = 1
    while True:
        yield i
        i += 1
for x in lista_infinita():
    print x
