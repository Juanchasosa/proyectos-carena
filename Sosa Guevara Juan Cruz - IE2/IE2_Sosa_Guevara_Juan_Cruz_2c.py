cont1, cont2 = 0, 0
acum1, acum2 = 0, 0

while True :
    valor = input("Ingrese un valor entero entre -30 y 0: ")

    if valor.isdigit() or valor.startswith("-") and valor[1:].isdigit() :
        valor = int(valor)
    else :
        print("No ingresó un valor entero")
        continue

    if valor == 50 :
        break

    if valor < -30 or valor > 0 :
        print("Valor fuera de rango")
        continue

    if valor > -10 :
        acum2 = acum2 + valor
        cont2 += 1

    cont1 += 1
    acum1 = acum1 + valor

print("===============================================")
print("Ingresaste", cont1,"valores entre -30 y 0")
print("El total acumulado de esos valores es: ", acum1)
print("===============================================")
print("Ingresaste", cont2,"valores entre -10 y 0")
print("El total acumulado de esos valores es: ", acum2)
print("===============================================")

