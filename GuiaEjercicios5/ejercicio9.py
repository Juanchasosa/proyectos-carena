from colorama import Back, Fore, init
init(True)

texto = "Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo."

print("\n")
print(texto)
print("\n")

for letra in texto :
    if letra.lower() == "a" or letra.lower() == "á" :
        print(Fore.BLUE + letra, end="")

    elif letra.lower() == "e" or letra.lower() == "é" :
        print(Fore.CYAN + letra, end="")

    elif letra.lower() == "i" or letra.lower() == "í" :
        print(Fore.GREEN + letra, end="")

    elif letra.lower() == "o" or letra.lower() == "ó" :
        print(Fore.MAGENTA + letra, end="")

    elif letra.lower() == "ú" or letra.lower() == "ú" :
        print(Fore.RED + letra, end="")
    else : print(letra, end="")