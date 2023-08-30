#Desarrollar un algoritmo para determinar el mayor de dos números enteros, que pueden ser distintos o iguales.

print("==============================================================================================")
print("En éste programa vamos a encontrar el mayor de 2 números o por otro lado, si ambos son iguales")
print("==============================================================================================")

a = int(input("Ingrese un número: "))
b = int(input("Ingrese un 2do número: "))

if a > b:
    print("El número más grande es: ", a)
elif a == b:
    print("Ambos números son iguales")
else:
    print("El número más grande es: ", b)