# -*- coding: utf-8 -*-
S='_|?|_|?|_|?|_|?|_|?|_|?|_|?|'
C = -20
iC = 5
while C <= 40:
    F = (9.0/5)*C + 32
    print C, F
    #C = C + iC
    C += iC
print S

#for each esta mas cool
gradosC = [-20, -15, -10, -5, 0, 5, 10 ,15, 20]
print '     C   F'
for grado in gradosC:
    F = (9.0/5)*grado + 32
    print '%5d %5.1f' % (grado, F)
print S

indice = 0
print '     C   F'
while indice < len(gradosC):
    C = gradosC[indice]
    F = (9.0/5)*C + 32
    # print C, F
    print '%5d %5.1f' % (C,F)
    indice+=1
print S
#recorren elementos de una lista y van procesando los valores uno al vez

gradosC = []
for C in range(-20,45,5):
    gradosC.append(C)
print gradosC
print S

gradosC = []
for i in range(0,31):
    C = -20 + i*2.5
    gradosC.append(C)
print gradosC
print S

#gradosC=[-20]
#L=[-20]
#while L[len(L)-1] != 30:
#    L.append(L[len(L)-1]+2.5)
print S


#Clase 11 delunes 21/01/2019 sibre listas
def listaC(Cmin, Cmax, n):
    gradosC = []
    dC = (Cmax - Cmin)/float(n-1)
    # for(i=0;i<n;i++)
    for i in range(n):
        C = Cmin + i*dc
        gradosC.append(C)
    return gradosC
