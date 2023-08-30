# Importar una libreria para obtener la raiz cuadrada
import math

# Ingresa el cateto a y lo guarda en la variable A
A = int(input("Ingrese el cateto A: "))

# Ingresa el cateto b y lo guarda en la variable B
B = int(input("Ingrese el cateto B: "))

# Calcula y guarda el resultado en C
C = math.sqrt(A ** 2 + B ** 2)

print("La hipotenusa es: ", C)