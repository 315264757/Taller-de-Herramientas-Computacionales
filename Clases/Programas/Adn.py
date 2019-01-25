# !/usr/bin/python
# -*- coding: utf-8 -*-

def contar_v1(adn,base):
    adn = list(adn)
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i

def contar_v2(adn,base):
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i

def contar_v3(adn,base):
    i = 0
    j = 0
    for j in (len(adn)):
        if adn[j] == base:
            i += 1
    return i

def contar_v4(adn,base):
    i = 0
    j = 0
    while j < (len(adn)):
        if adn[j] == base:
            i += 1
        j += 1
    return i




adn = 'ATGCGACCTAT'
base = 'C'
print contar_v1(adn,base)

n = contar_v2(adn.base)
print n
print '%s aparece %d veces en %s' \
      % (base, n, adn)
print '{base} aparece {n} veces en {adn}'.\
      format(base=base,n=n,adn=adn)
print contar_v2(adn, base)
print contar_v3(adn, base)
print contar_v4(adn, base)
