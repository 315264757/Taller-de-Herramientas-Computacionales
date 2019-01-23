# !/usr/bin/python
# -*- coding: utf-8 -*-

alumnos = []
a = [9,8,10,9]
b = [9]
c = [6,9,10,8,9,10,10,9]
alumnos.append(a)
alumnos.append(b)
alumnos.append(c)
print(alumnos)

alumnos1 = []
alumnos1.extend(a)
alumnos1.extend(b)
alumnos1.extend(c)
print alumnos1

for i in range(len(alumnos)):
    for j in  range(len(alumnos[i])): #con el corchete no es necesario definir a,b,c
        calificacion = alumnos[i][j] #de la iesima lista estoy obtiendo el jesimo elemento
        print '%4d' % calificacion,
    print

alumnos1.sort()
print alumnos1
