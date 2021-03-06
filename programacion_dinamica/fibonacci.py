import sys

def fibonacci_recursivo(n):
    if n == 0 or n ==1:
        return 1
    
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def fibonacci_dinamico(n,nemo = {}):
    if n == 0 or n == 1:
        return 1

    try:    
        return nemo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, nemo) + fibonacci_dinamico(n-2)
        nemo[n] = resultado
        return resultado


if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    n= int(input('Escoge un numero:  '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
    fibonacci_dinamico(n)