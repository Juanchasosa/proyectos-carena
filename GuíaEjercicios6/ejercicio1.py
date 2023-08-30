import random

v1 = []
v2 = []
v3 = []

mayorv2, mayorv3 = 0, 0
menorv2, menorv3 = 100, 100


for i in range(0, 20) :
    numero = random.randint(10, 99)
    v1.append(numero)


for numero in v1 :
    if numero % 2 == 0 :
        v2.append(numero)
    else :
        v3.append(numero)

for numero in v2 :
    if numero > mayorv2 :
        mayorv2 = numero

    elif numero < menorv2 :
        menorv2 = numero

for numero in v3 :
    if numero > mayorv3 :
        mayorv3 = numero

    elif numero < menorv3 :
        menorv3 = numero

print(v1)
print(v2)
print(v3)

print("=============================================")
print("El número mayor de la lista 2 es: ", mayorv2)
print("Se encuentra en la posición: ", v2.index(mayorv2))
print("El número menor de la lista 2 es: ", menorv2)
print("Se encuentra en la posición: ", v2.index(menorv2))

print("\n")

print("El número mayor de la lista 3 es: ", mayorv3)
print("Se encuentra en la posición: ", v3.index(mayorv3))
print("El número menor de la lista 3 es: ", menorv3)
print("Se encuentra en la posición: ", v3.index(menorv3))
print("=============================================")
