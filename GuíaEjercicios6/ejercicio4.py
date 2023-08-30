import random

# Inicializar las matrices v1 y v2
v1 = [[0 for _ in range(5)] for _ in range(5)]
v2 = [[0 for _ in range(5)] for _ in range(5)]

# Cargar las matrices con números al azar
for f in range(5):
    for c in range(5):
        v1[f][c] = random.randint(0, 99)
        v2[f][c] = random.randint(0, 99)

# Mostrar la matriz v1
print("Matriz v1:")
for f in range(5):
    for c in range(5):
        print('{:>2}'.format(v1[f][c]), end=" ")
    print()

# Mostrar la matriz v2
print("\nMatriz v2:")
for f in range(5):
    for c in range(5):
        print('{:>2}'.format(v2[f][c]), end=" ")
    print()
