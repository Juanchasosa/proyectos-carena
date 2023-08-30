# Desarrollar un algoritmo para calcular el promedio de una serie de valores enteros.

acum = 0
contador = 0

while True :

    valor = int(input("Ingrese un valor entre 10 y 99: "))

    if valor == 0 :
        break

    if valor < 10 or valor > 99 :
            print("Valor fuera de rango")
            continue

    contador += 1
    acum = acum + valor

resultado = acum / contador
print(resultado)