import random

mayor1, mayor2 = 0, 0
menor1, menor2 = 801, 601
acumulador1, acumulador2 = 0, 0
contador1, contador2 = 0, 0

for i in range(1, 21) :
    numero = random.randint(200, 800)
    print(i, numero)

    if numero > mayor1 :
        mayor1 = numero

    if numero < menor1 :
        menor1 = numero

    if numero > 400 and numero < 600 :
        acumulador2 += numero
        contador2 += 1
        if numero > mayor2 :
            mayor2 = numero
        if numero < menor2 :
            menor2 = numero

    acumulador1 += numero
    contador1 += 1

promedio = acumulador1 / contador1
promedio2 = acumulador2 / contador2




print("El número mayor es: ", mayor1)
print("El número menor es: ", menor1)
print("El promedio total es: ", promedio)

print("=================================")
print("Mayores que 400 y menores que 600")
print("=================================")
print("El promedio de los numeros mayores que 400 y menores que 600 es: ", promedio2)
print("El número mayor es: ", mayor2)
print("El número menor es: ", menor2)