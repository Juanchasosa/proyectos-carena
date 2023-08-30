import random

for i in range(1, 21) :
    numero = random.randint(100, 999)
    print(i, "-", numero)

    if numero % 2 == 0 :
        print("*", numero)

    if numero % 3 == 0 :
        print("#", numero)

    if numero % 4 == 0 :
        print("$", numero)
    if numero % 5 == 0 :
        print("&", numero)