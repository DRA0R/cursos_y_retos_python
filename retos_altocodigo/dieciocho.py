
cadena = str(input('Ingrese la cadena, para medir su longitud: '))

def longitud_cadena():    
    longitud = len(cadena)
    print(longitud)

def mayus():
    print(cadena.capitalize())

longitud_cadena()
mayus()