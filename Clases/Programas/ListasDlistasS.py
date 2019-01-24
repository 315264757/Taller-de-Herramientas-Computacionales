# !/usr/bin/python
# -*- coding: utf-8 -*-

from ListasDlistas import *

print 'Debes ingresar aignaturas diferentes para que los datos se guarden correctamente'
print 'La lista de la asignatura lleva de orden; asistencias, tareas, calificacion'

clave = input("Clave del alumno")
sem = input("Ingresa el semestre que cursa el alumno para guardar las asignaturas")

asig1 = input("Primer asignatura")
asist1 = input("Asistencias del alumno")
tar1 = input("Numero de tareas que el alumno presento")
cali1 = input("Calificacion final") 

asig2 = input("Segunda asignatura")
asist2 = input("Asistencias del alumno")
tar2 = input("Numero de tareas que el alumno presento")
cali2 = input("Calificacion final")


traye = alumno(sem,asig1,asig2,asist2,tar2,cali2,asist1,tar1,cali1)

print 'Es la trayectoria del alumno %d' % (clave) 



