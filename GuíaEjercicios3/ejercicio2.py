import random

cont1, cont2, cont3 = 0, 0, 0
acum1, acum2, acum3 = 0, 0, 0

for i in range(1,31) :
    numero = random.randint(0, 999)

    if numero >= 0 and numero <= 300 :
        acum1 = acum1 + numero
        cont1 += 1

    if numero >= 301 and numero <= 600 :
        acum2 = acum2 + numero
        cont2 += 1

    if numero >= 601 and numero <= 1000 :
        acum3 = acum3 + numero
        cont3 += 1
    print (i, ":", numero)

print("Se generaron un total de:", cont1, " números entre 0 y 300")
print("El resultado de la suma de todos los números entre 0 y 300 es: ", acum1)

print("Se generaron un total de:", cont2, " números entre 301 y 600")
print("El resultado de la suma de todos los números entre 301 y 600 es: ", acum2)

print("Se generaron un total de:", cont3, "números entre 601 y 1000")
print("El resultado de la suma de todos los números entre 601 y 1000 es: ", acum3)