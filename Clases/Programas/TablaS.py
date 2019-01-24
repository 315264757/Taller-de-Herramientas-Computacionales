# !/usr/bin/python
# -*- coding: utf-8 -*-

from Grados import *
from pprint import pprint

gradosC = listaC(-5,0.5,5)
gradosF = listaF(gradosC)

tabla = [[C,F] for C,F in zip(gradosC,gradosF)]
print(tabla)

#El programa está casi completo, solo falta agragarle el vector de direccion y un freno para el tiro horizpntal

pprint(tabla)
