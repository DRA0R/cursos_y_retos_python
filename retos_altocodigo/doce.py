from abc import abstractproperty


lista_1 = []
lista_2 = []

for i in range(1,11):
    lista_1.append(i)
for i in range (11,21):
    lista_2.append(i)

suma_listas = lista_1 + lista_2
print(suma_listas)
print(lista_1)
print(lista_2)