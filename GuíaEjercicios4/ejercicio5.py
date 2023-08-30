import random

acum = 0
cont = 0
for i in range(1, 21) :

    numero = random.randint(100, 999)

    if numero >= 300 and numero <= 700 :
        print(numero)
    acum = acum + i
    cont += 1

print("La cantidad de vueltas es: ", cont)
print("La suma de los valores de esas vueltas es: ", acum)