cont1, cont2 = 0, 0
acum1, acum2 = 0, 0

while True:

    numero = int(input("Ingrese un número entre 1 y 999: "))

    if numero == 0 :
        break

    if numero < 1 or numero > 999 :
        print("Valor fuera de rango")
        continue

    if numero != 0 and numero <= 500 :
        acum1 = acum1 + numero
        cont1 += 1
    if numero > 500 :
        acum2 = acum2 + numero
        cont2 += 1

print("Se ingresaron", cont1, "números menores o iguales a 500")
print("La suma de todos esos números es: ", acum1)
print("=======================================================")
print("Se ingresaron", cont2, "números mayores a 500")
print("La suma de todos esos números es: ", acum2)
