#Desarrollar un algoritmo para el cálculo de la hipotenusa

import math

print("========================")
print("Calculo de la hipotenusa")
print("========================")

catetoA = int(input("Ingrese el cateto A: "))
catetoB = int(input("Ingtese el cateto B: "))

c = math.sqrt(catetoA ** 2 + catetoB ** 2)

print("El resultado de la hipotenusa es igual a: ",c)