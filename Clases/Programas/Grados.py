# !/usr/bin/python
# -*- coding: utf-8 -*-

#Clase 11 delunes 21/01/2019 sibre listas
def listaC(Cmin, Cmax, n):
    gradosC = []
    dC = (Cmax - Cmin)/float(n-1)
    # for(i=0;i<n;i++)
    for i in range(n):
        C = Cmin + i*dC
        gradosC.append(C)
    return gradosC

def listaF(gradosC):
    gradosF = []
    for C in gradosC:
        F = (9.0/5)* C + 32
        gradosF.append(F)
    return gradosF

def mostrarListas(gradosC, gradosF):
    #se podria usar n=(len(grados)): y en la linea de abajo usar n pero no es tan eficiente
    for i in range(len(gradosC)):
        C = gradosC[i]
        F = gradosF[i]
        print "%5.1f %5.1f" % (C, F)

def mostrarListas1(gradosC, gradosF):
    for C, F in zip(gradosC, gradosF):
        print '%5d %5.1f' % (C,F)
