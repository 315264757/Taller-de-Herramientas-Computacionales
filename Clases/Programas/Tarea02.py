# -*+ coding: utf-8 -*-
# Hector Chaparro 315264757
import math

G = 6.67*10**(-11)
print '-La constante de gravitacion universal deducida por Isaac Newton es G=%g' % G
M = (4*(math.pi)**2*(1496*10**11)**3)/6.67*10**(-11)*31557.600**2
print '-La masa del sol es de M=%g\n' % M

print 'Calcula el tiempo que tarda un planeta en dar la vuelta al sol'
print 'Ingresa "periodo(distancia del planeta al sol,velocidad en la que viaja)"\n'
def periodo(r,v):
    t = 2*(math.pi)*r/v
    return(t)

print 'Calcula la velocidad en la que viaja un planeta'
print 'Ingresa "velocidad(distancia del planeta al sol, constante de gravitacion universal, masa del sol)"\n'
def velocidad(r,G,M):
    v = math.sqrt(G*M/r)
    return(v)

print 'Calcula la masa de un planeta'
print 'Ingresa "masa(distancia del planeta, velocidad en la que viaja el planeta, fuerza gravitacional que ejerce el sol sobre el planeta)"\n'
def masa(r,v,F):
    m = F*r/v**2
    return(m)

print 'Calcula la fuerza gravitacional que ejerce el sol sobre un planeta'
print 'Ingresar "fuerza(masa del planeta,distancia del planeta al sol, velocidad en la que viaja el planeta)"'
def fuerza(m,r,v):
    F = m*v**2/r
    return(F)

