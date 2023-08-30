cont1, cont2, cont3 = 0, 0, 0
acum1, acum2 = 0, 0

while True :
    temperatura = int(input("Ingrese una temperatura entre -20 y 50: "))

    if temperatura == 100 :
        break

    if temperatura < -20 or temperatura > 50 :
        print("Valor fuera de rango")
        continue

    if temperatura < 0 :
        acum1 = acum1 + temperatura
        cont1 += 1
    elif temperatura == 0 :
        cont3 += 1
    else :
        acum2 = acum2 + temperatura
        cont2 += 1

promedio1 = acum1 / cont1
promedio2 = acum2 / cont2

print("Ingresaste", cont3, "temperaturas iguales a 0°")
print("==============================================")
print("Ingresaste", cont1, "temperaturas menores a 0°")
print("El promedio de esas temperaturas ronda los: ", promedio1, "°")
print("==============================================")
print("Ingresaste", cont2, "temperaturas mayores a 0°")
print("El promedio de esas temperaturas ronda los: ", promedio2, "°")
