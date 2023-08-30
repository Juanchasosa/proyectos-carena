#Desarrollar un algoritmo para determinar el mayor de tres números distintos.

print("===================================================================")
print("En éste programa vamos a determinar el mayor de 3 números distintos")
print("===================================================================")

a = int(input("Ingrese un 1er valor: "))
b = int(input("Ingrese un 2do valor: "))
c = int(input("Ingrese un 3er valor: "))

if a > b :
    if a > c :
        print("El número más grande es: ", a)
    else:
        print("El número más grande es: ", c)
elif b > c :
    print("El número más grande es: ", b)
else:
    print("El número más grande es: ", c)

print("Fin del programa")