def diana(x,y):
    if x<=5 and (y<=10 or y>30):
        return(3)
    elif x>25 and (y<=10 or y>30):
        return(3)
    elif 5<x<=25 and (y<=10 or y>30):
        return(7)
    elif 10<y<=30 and (x<=5 or x>25):
        return(5)
    else:
        return(10)
