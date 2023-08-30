import random

cont = 0
acum = 0

max = 0
min = 900

for i in range(1,31) :
    numero = random.randint(300, 800)
    print(i, "->", numero)

    if numero % 4 == 0 :
        print("*", numero)

    if numero % 6 == 0 :
        print("#", numero)

    if numero >= 300 and numero <= 600 :
        cont += 1
        acum = acum + numero

    if numero >= 501 and numero <= 800 :

        if numero < min :
            min = numero
        elif numero > max :
            max = numero


promedio = acum / cont
print("El promedio de los numeros entre 300 y 600 inclusive es: ", promedio)
print("El numero menor entre 501 y 800 inclusive es: ", min)
print("El numero mayor entre 501 y 800 inclusive es: ", max)