#Programa de piedra papel y tijera
# Lograr que el pc seleccione al azar entre las 3 variables y enfrentarlo
#contra la opcion que seleccione el usuario
import random

opciones = [1,2,3]
valor = ['piedra', 'papel', 'tijeras']
numero_usuario = int(input(print('selecciona: \n1. piedra \n2. papel \n3. tijeras \n')))
usuario = opciones[numero_usuario-1]
maquina = random.choice(opciones)

print(f'Tu selecionaste: {valor[usuario-1]}')
print(f'La maquina seleciciono: {valor[maquina-1]}')


def pelea(u, m):
    if usuario == maquina:
        print('Empate')

    elif usuario != maquina:
        if usuario == 1 and maquina == 3:
            print('Ganaste')
        elif usuario == 2 and maquina == 1:
            print('Ganaste')
        elif usuario == 3 and maquina == 2:
            print('Ganaste')
        else: print('PERDISTE')

pelea(usuario, maquina)