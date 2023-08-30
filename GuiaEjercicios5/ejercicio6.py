from colorama import Back, Fore, init
init(True)

texto = "Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo."

print("\n")
print(texto)
print("\n")

cadena = "aeiou"

for x in texto :
    if cadena.find(x.lower()) != -1 :
        print(Fore.RED + x, end="")
    else:
        print(x, end="")