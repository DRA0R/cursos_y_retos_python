numero = []
numero_2 = []
total_numeros = []
sumita = []
x = False

while x == False:
    numero = float(input('Ingrese su numero: '  ))
    numero_2 = float(input('Ingrese el valor porcentual: '))

    media = numero * numero_2 / 100
    total_numeros.append(media)

    sumita.append(numero_2)
    cambiador = sum(sumita)

    if  cambiador >= 100:
        x = True
    

media_porcentual = sum(total_numeros)

print('Esta es la media de los numeros dados: ' + str(media_porcentual))