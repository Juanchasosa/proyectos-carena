cont1, cont2, contCeros = 0, 0, 0
acum1, acum2 = 0, 0
while True :

    temp = input("Ingrese una tempertura entre -20 y 50: ")

    #VALIDACIÓN=============================================
    if temp.startswith("-") and temp[1:].isdigit() or temp.isdigit() :
        temp = int(temp)
    else:
        print("No se ingresó un valor numérico")
        continue

    if temp == 100 :
        break

    if temp < -20 or temp > 50 :
        print("Valor fuera de rango")
        continue
    #VALIDACIÓN=============================================


    if temp < 0 :
        cont1 += 1
        acum1 += temp

    elif temp > 0 :
        cont2 += 1
        acum2 += temp

    else :
        contCeros += 1


promBajoCero = acum1 / cont1
promSobreCero = acum2 / cont2

print("====================================================================")
print("El promedio de las temperaturas bajo 0 es igual a: ", promBajoCero)
print("El promedio de las temperaturas sobre 0 es igual a: ", promSobreCero)
print("Se ingresaron", contCeros, "temperaturas iguales a 0")
print("====================================================================")
