#def paridad(x):
#    if x/2 == d and 2*d == x :
#        return(si)
#    else:
#        return(no)

        
#def sucULAM(x):
#    a = x/2
#    b = 3*x+1
#    while :
#        if paridad(si):
#            print(a)
#        else :
#            print(b)


        
def ulam(x):
    if(x/2)*2 == 0: 
        return x/2
    else:
        return 3*x + 1
#el problema lo dividimos en partes para ir splocuinando eficazmente

def suc(x):
    while x>1: #while x>1: (tambien asi se puede)
        x=ulam(x)
        print x

print ulam(52)
print suc(17)
print suc(26)
print suc(52)
print suc(1024)
print suc(72)
print suc(1524927)
print suc(2)
#al final ponemos los dos print para los resultados de las funciones
