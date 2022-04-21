import random

opciones = [1,2,3]
valor = ['piedra', 'papel', 'tijeras']

numero_usuario = int(input(print('selecciona un numero del 1 al 3: \n1. piedra \n2. papel \n3. tijeras \n')))
usuario = numero_usuario
maquina = random.choice(opciones)

def deco(func):
    def wrapper(*args,**kwargs):
        print(f'Tu selecionaste: {valor[usuario-1]}')
        print(f'La maquina seleciciono: {valor[maquina-1]}')
        func(*args,**kwargs)
        return wrapper

@deco
def pelea(u, m):
    if u == m:
        print('Empate')
    elif u != m:
        if u == 1 and m == 3:
            print('Ganaste')
        elif u == 2 and m == 1:
            print('Ganaste')
        elif u == 3 and m == 2:
            print('Ganaste')
        else: print('PERDISTE')

pelea(usuario, maquina)