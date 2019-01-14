# -*+ coding: utf-8 -*-
# Hector Chaparro 315264757
# Problema: Calcular la masa del sol dada la distancia de la tierra al sol

import math
print (4*(math.pi)**2*(1496*10**11)**3)/6.67*10**(-11)*31557.600**2
print (4.0*(math.pi)**2.0*(1496.0*10.0**11.0)**3.0)/6.67*10.0**(-11)*31557.600**2.0

pi = (math.pi)          
r = 1496.0*10**11       # Distancia de la tierra al sol
G = 6.67*10**(-11)      # Coeficiente de gravitacion universal
t = 31557.600           # Tiempo que tarda la tierra en dar la  vuelta al sol en segundos 

M = 4*(pi**2)*(r**3)/G*t**2 # Masa del sol
print M

def 
