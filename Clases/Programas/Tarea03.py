import math

def diana(x,y):
    if x<=5 and ((y<=10 or y>30) or (y<=10 or y>30)):
        return(3)
    elif 5<x<=25 and (y<=10 or y>30):
        return(7)
    elif 10<y<=30 and (x<=5 or x>25):
        return(5)
    elif (x,y)>2*math.pi*r and (15,20):
        return(10)
    else:
        return(100)

#Intentos fallidos

#   elif (x-15)**2+(y-20)**2:
#       return (10)
#   elif (15.20) with math.pi*10**2:
#       return(10)
#   elif (x**2+y**2+(-30)*x+(-40)*y+525) with x=15 and y=20:
#      return (10)    
