

def fib(n):
        """Calcula el enesimo termino
de suc de fib con n natural
"""
        if n>2:
            return fib(n-1) + fib(n-2)
        else:
            return 1
fib(1)
fib(2)
fib(5)
fib(10)


def sigma(k):
    """Calcula el enesimo termino
de la suma de naturales
"""
    if k > 1:
        return(k + sigma(k-1))
    else:
        return(1)
