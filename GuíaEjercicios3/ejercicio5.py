import random

cont1, cont2 = 0, 0
acum1, acum2 = 0, 0

for i in range(1, 31) :

    numero = random.randint(1, 99)

    if numero % 2 == 0 :
        print ("*", numero)
        acum1 = acum1 + numero
        cont1 += 1
    else :
        print("#", numero)
        acum2 = acum2 + numero
        cont2 += 1


print("Se generaron un total de", cont1, "números pares")
print("El resultado de la suma de todos los números pares es: ", acum1)
print("Se generaron un total de", cont2, "números impares")
print("El resultado de la suma de todos los números impares es: ", acum2)