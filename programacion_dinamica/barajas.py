import random
import collections

PALOS =['picas', 'corazones', 'diamantes', 'treboles','picas', 'corazones', 'diamantes', 'treboles']

VALORES = ['as','2', '3', '5','6', '7', '8','9', '10', 'jota', 'qu','ka'] #De ser solo uno seria medio naipe

def crear_baraja():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((valor,palo))
    return barajas


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)


    if calculador == 1:
        pares = 0
        for mano in manos:
            valores = []
            for carta in mano:
                valores.append(carta[0])
                
            counter = dict(collections.Counter(valores))
            print(counter)
            for val in counter.values():
                if val == 2:
                    pares += 1
                    break

        probabilidad_par = pares / intentos
        print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')

    elif calculador == 2:
        pares_dobles = 0
        for mano in manos:
            valores = []
            for carta in mano:
                valores.append(carta[0])

            counter = dict(collections.Counter(valores))
            for val in counter.values():
                if val == 2:
                    
                    pares_dobles += 1

                    break

    elif calculador == 3:
        tercia = 0
        for mano in manos:
            valores = []
            for carta in mano:
                valores.append(carta[0])

            counter = dict(collections.Counter(valores))
            for val in counter.values():
                if val == 3:
                    tercia += 1
                    break

        probabilidad_tercia = tercia / intentos
        print(f'La probabilidad de obtener una tercia en una mano de {tamano_mano} barajas es {probabilidad_tercia}')

    elif calculador == 4:
        '''escalera = 0
        for mano in manos:
            valores = []
            for carta in mano:
                valores.append(carta[0])

            counter = dict(collections.Counter(valores))
            for val in counter.values():
                if val == 3:
                    escalera += 1
                    break'''

    elif calculador == 5:
        corrida = 0
        for mano in manos:
            palos = []
            for carta in mano:
                palos.append(carta[1])

            counter = dict(collections.Counter(palos))
            for pal in counter.values():
                if pal == 5:
                    corrida += 1
                    break

            probabilidad_corrida = corrida / intentos
        print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} barajas es {probabilidad_corrida}')

    elif calculador == 6:
        pass

    elif calculador == 7:
        pass

    elif calculador == 8:
        pass

    elif calculador == 9:
        pass


    

if __name__ == '__main__':

    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos quieres para calcular la probabilidad: '))

    calculador = int(input('Que probabilidad desea calcular? \n Digite  \n 1: Par \n 2: Doble par \n 3: Tercia \n 4: Escalera \n 5: Corrida \n 6: Full house \n 7: Poquer \n 8: Escalera de color \n 9: Escalera real \n' ))
        
    main(tamano_mano, intentos)

    barajas = crear_baraja()
    mano = obtener_mano(barajas, 5)