def vAbsoluto(x):
    if x>=0:
        return(x)
    else:
        return(-x)

def raiz(x):
    h=x
    b=1.0
    e=0.0001
    while vAbsoluto(b-h)>e:
        h = (b+h)/2
        b = x/h
    return(b)

print raiz(1.0)
print raiz(4.0)
print raiz(9.0)
print raiz(9.1)
print raiz(1000000.0)

def raiz1(x):
    h=x
    b=1.0
    e=0.0001
    i=0 #cuenta el numero de veces que se ejecuta el ciclo
    while vAbsoluto(b-h)>e:
        i=i+1
        h = (b+h)/2
        b = x/h
    print "El ciclo se repitio %d veces"% (i)
    return(b)

print raiz1(1.0)
print raiz1(4.0)
print raiz1(9.0)
print raiz1(9.1)
print raiz1(1000000.0)

