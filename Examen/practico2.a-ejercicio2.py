
contador1, contador2 = 0, 0
acum1, acum2 = 0, 0

while True :
    a = int(input("Ingrese un número para a: "))

    if a == 100 :
        break


    if a >= -40 or a >= 40 :
        acum1 += a
        contador1 += 1
    if a < 0 :
        contador2 += 1
        acum2 += a
        continue







print("Cantidad de valores ingresados: ", contador1)
print("Cantidad total: ", acum1)

print("Cantidad de valores ingresados menores a 0: ", contador2)
print("Cantidad total de números menores a 0: ", acum2)

