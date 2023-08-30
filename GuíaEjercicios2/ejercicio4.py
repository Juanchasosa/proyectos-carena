#Desarrollar un algoritmo para determinar el mayor de tres números, puede haber iguales.

print("===================================================================")
print("En éste programa vamos a determinar el mayor de 3 números distintos")
print("===================================================================")

a = int(input("Ingrese un 1er valor: "))
b = int(input("Ingrese un 2do valor: "))
c = int(input("Ingrese un 3er valor: "))

if a == b :
    if a == c :
        print("Los números a, b y c son iguales")
    elif a > c :
        print("Los números más grandes son a y b: ", a)
    else :
        print("El mayor es c: ", c)
elif a == c :
    if a > b :
        print("Los números más grandes son a y c: ", a)
    else :
        print("El número más grande es b: ", b)
elif a > b :
    if a > c :
        print("El número más grande es a: ", a)
    else :
        print("El número más grande es c: ", c)
else:
    if b > c :
        print("El número más grande es b: ", b)
    else :
        print("El número más grande es c: ", c)