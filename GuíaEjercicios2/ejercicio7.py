#Desarrollar un algoritmo para calcular las tablas de multiplicar del 1 al 10 en el rango de 1 a 10.

print("====================")
print("tabla de multiplicar")
print("====================")

while True  :
    contador = 1

    tabla = int(input("Ingrese el número de la tabla a calcular: "))

    if tabla == 0 :
        break

    while contador <= 10 :
        resultado = tabla * contador
        print(tabla, "x", contador, "=", resultado)
        contador += 1

print("Fin")
