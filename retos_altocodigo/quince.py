numeros_media = []
x = False

while x == False:
    numero = float(input('Ingrasa un numero, master: \n para calcular escribe media "N"'  ))
    numeros_media.append(numero)
    if numero == -1:
        x = True

media = sum(numeros_media) / len(numeros_media)
print('Esta es la media de los numeros dados: ' + str(media))