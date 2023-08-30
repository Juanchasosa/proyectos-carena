cont1, cont2, cont3= 0, 0, 0
acum1, acum2 = 0, 0

while True :
    nota = int(input("Ingrese la nota entre 1 y 10: "))

    if nota == -1 :
        break

    if nota < 1 or nota > 10 :
        print("Valor fuera de rango")
        continue

    if nota < 7 :
        cont1 += 1
        acum1 = acum1 + nota

    elif nota == 7 :
        cont2 += 1

    else :
        acum2 = acum2 + nota
        cont3+=1

promedio1 = acum1 / cont1
promedio2 = acum2 / cont3

print("=====================================================")
print("Hay un total de", cont1, "notas menores a 7")
print("El promedio de las notas menores a 7 es :", promedio1)
print("=====================================================")
print("Hay un total de", cont3, "notas mayores a 7")
print("El promedio de las notas mayores a 7 es :", promedio2)
print("=====================================================")
print("Hay un total de", cont2, "notas iguales a 7")
print("=====================================================")


