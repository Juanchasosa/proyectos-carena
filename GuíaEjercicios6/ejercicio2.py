import random

lista = []
mayor1, mayor2 = 0, 0
menor1, menor2 = 100, 100

for i in range(0, 20) :
    numero = random.randint(10, 99)
    lista.append(numero)


for numero in lista[0:9] :
    if numero > mayor1 :
        mayor1 = numero
    elif numero < menor1 :
        menor1 = numero

for numero in lista[10:20] :
    if numero > mayor2 :
        mayor2 = numero
    elif numero < menor2 :
        menor2 = numero




print(lista)

print("=================================================")
print("De los primeros 10 números el mayor es :", mayor1)
print("Su posición es: ", lista.index(mayor1))
print("De los primeros 10 números el menor es :", menor1)
print("Su posición es: ", lista.index(menor1))

print("\n")

print("De los últimos 10 números el mayor es: ", mayor2)
print("Su posición es: ", lista.index(mayor2))
print("De los últimos 10 números el menor es: ", menor2)
print("Su posición es: ", lista.index(menor2))
print("=================================================")