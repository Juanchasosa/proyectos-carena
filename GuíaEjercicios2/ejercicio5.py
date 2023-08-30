# Desarrollar un algoritmo para permitir el ingreso de una serie de números enteros positivos, hasta que el usuario ingrese el número 0, determinar cuál es el mayor.
print("=============================================================")
print("Bienvenido, hoy buscaremos el mayor de varios números enteros")
print("=============================================================")

mayor = 0
primero = True

while True :
    a = int(input("Ingrese un número para a: "))

    if a == 0 :
        break

    if primero :
        mayor = a
        primero = False

    if a > mayor :
        mayor = a
        continue

print("El número mayor es: ", mayor)