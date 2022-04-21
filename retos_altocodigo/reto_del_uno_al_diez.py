valores_suma=[]
suma = 0

for i in range(200,401,5):
    print(i)
    valores_suma.append(i)
    
for i in valores_suma:
    suma += i
print('esta es su suma')
print(suma)

