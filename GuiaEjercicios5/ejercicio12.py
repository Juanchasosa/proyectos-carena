from colorama import Back, Fore, init
init(True)

texto = "él Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo."

print("\n")
print(texto)
print("\n")

lista = texto.split()

acentos = "áéíóú"
contar = 0

for palabra in lista :
    flag = False

    for letra in palabra :
        if letra.lower() in acentos :
            contar += 1
            flag = True
            break

    if flag :
        print(Fore.RED + palabra, end=" ")
    else:
        print(palabra, end=" ")

print("\n")
print("Se encontraron", contar, "palabras que contienen acento")