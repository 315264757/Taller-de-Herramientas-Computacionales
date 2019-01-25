# !/usr/bin/python
# -*- coding: utf-8 -*-

def primo(p):
    for i in range (2,p):
        if p%i == 0:
            print 'no es primo'
            break
        else:
            print 'es primo'
            break
# me tarde un rato hacieno este ya que no recordaba que podia usar el % para checar divisibilidad
