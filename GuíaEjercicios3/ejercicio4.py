vueltas = 0
cont1, cont2 = 0, 0
acum1, acum2 = 0, 0

while True :

    numero = int(input("Ingrese un valor entre 1 y 100: "))

    if numero == -1 :
        print("No se ingresaron 12 numeros")
        break

    if vueltas == 12 :
        break

    if numero < 1 or numero > 100 :
        print("Valor fuera de rango")
        continue


    if numero % 2 == 0 :
        acum1 = acum1 + numero
        cont1 += 1
    else :
        acum2 = acum2 + numero
        cont2 += 1

    vueltas += 1


print("Ingresaste", cont1, "números divisibles por 2")
print("El valor total de la suma de esos números es: ", acum1)

print("Ingresaste", cont2, "números que no son divisibles por 2")
print("El valor total de la suma de esos números es: ", acum2)