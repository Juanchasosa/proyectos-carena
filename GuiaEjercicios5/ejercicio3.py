from colorama import Fore, init
init(True)

texto = "un Unos Unas una Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo."

print("\n")
print(texto)
print("\n")

lista = texto.split()
articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas"]
verificador = False

# for palabra in lista :
#     if palabra == "el" or palabra == "la" or palabra == "los" or palabra == "las" or palabra == "un" or palabra == "una" or palabra == "unos" or palabra == "unas" :
#         print(Fore.RED + palabra + " ", end="")
#     else:
#         print(palabra + " ", end="")

for palabra in lista :
    for articulo in articulos :
        if palabra.lower() == articulo :
            verificador = True
    if verificador :
        print(Fore.RED + palabra + " ", end="")
        verificador = False
    else:
        print(palabra + " ", end="")
