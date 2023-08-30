import random
cont2, cont4, cont3, cont5 = 0,0,0,0
acum2 = acum3 = acum4 = acum5 = 0

for i in range(0, 20) :
    numero = random.randint(100, 999)
    print(i, numero)


    if numero % 2 == 0 :
        cont2 += 1
        acum2 += numero

    if numero % 3 == 0 :
        cont3 += 1
        acum3 += numero

    if numero % 4 == 0 :
        cont4 += 1
        acum4 += numero

    if numero % 5 == 0 :
        cont5 += 1
        acum5 += numero


print ("Cantidad de números divisibles por 2:", cont2, " Valores totales acumulados :", acum2)
print ("Cantidad de números divisibles por 3:", cont3, " Valores totales acumulados :", acum3)
print ("Cantidad de números divisibles por 4:", cont4, " Valores totales acumulados :", acum4)
print ("Cantidad de números divisibles por 5:", cont5, " Valores totales acumulados :", acum5)