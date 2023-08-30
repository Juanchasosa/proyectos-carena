#Desarrollar un algoritmo para determinar el mayor de dos números enteros distintos.

print("========================================================")
print("En éste programa vamos a encontrar el mayor de 2 números")
print("========================================================")

a = int(input("Ingrese un número: "))
b = int(input("Ingrese un 2do número: "))

if a > b:
    print("El número más grande es: ", a)
else:
    print("El número más grande es: ", b)