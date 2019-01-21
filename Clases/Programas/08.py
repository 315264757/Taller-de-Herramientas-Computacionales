#!/usr/bin/python2.7
# -*+ coding: utf-8 -*-
#""" se refiere a hacer una cadena y a cerrarla
print "Héctor Chaparro Reza"+"\n315264757"+"\nTaller de Herramientas Computacionales" 

x = 10.5;y = 1.0/3;z = 15.3
#x,y,z=10.5,1.0/3,15.3 modo de asignar variables caracteristica d e python
H = """
El punto en R3 es:
(x,y,z)=(%.2f,%g,%G)
""" % (x,y,z)
print H


#probar sin el parentesis en linea abajo de El punto en R3 es:
#poner etiqueta luego dos puntos y la letra de como quiero que me lo muestre (flotante)

G="""
El punto en R3 es:
(x,y,z)={laX:.2f},{laY:g},{laZ:G} 
""".format(laX=x,laY=y,laZ=z)
print G

#Conversion de tipos
print 'Algo ' + str(x)

print float(str(x))*3
#print 'x es de tipo %s' % type(x)._name_
print type(5)
print type('5')

print "Coordenadas de la flecha\n"
x=input("¿Cual es la abcisa?\n")
y=input("¿Cual es la ordenada?\n")
