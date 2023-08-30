acum = 0
cont = 0

while True :
    numero = int(input("Ingrese un número entre 100 y 500 inclusive: "))

    if numero == -1 :
        break

    if numero < 100 or numero > 500 :
        print("Valor fuera de rango")
        continue

    acum = acum + numero
    cont += 1

promedio = acum / cont

print("El promedio de los números ingresados es: ", promedio)