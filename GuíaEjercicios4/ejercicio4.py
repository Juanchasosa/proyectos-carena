import random

menor1, menor2 = 500, 999
mayor1, mayor2 = 0, 0

for i in range(1, 21) :
    numero = random.randint(100, 999)
    print(i, "=", numero)

    if numero < 500 :
        if numero < menor1 :
            menor1 = numero
        elif numero > mayor1 :
            mayor1 = numero

    if numero > 500 :
        if numero < menor2 :
            menor2 = numero
        elif numero > mayor2 :
            mayor2 = numero

print("El numero menor de los menores a 500 es: ", menor1)
print("El numero menor de los mayores a 500 es: ", menor2)
print("===================================================")
print("El numero mayor de los mayores a 500 es: ", mayor2)
print("El numero mayor de los mayores a 500 es: ", mayor1)