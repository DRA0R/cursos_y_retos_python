import random
numeros_totales = [ i for i in range (1,101)]

numero_aleatoreo = random.choice(numeros_totales)
print(numero_aleatoreo)

numero_ingresado = 0

while numero_ingresado != numero_aleatoreo:
    numero_ingresado = int(input('Ingresa un numero del 1 al 100: '))

    if numero_ingresado == numero_aleatoreo:
        print('Adivinaste!')
        break