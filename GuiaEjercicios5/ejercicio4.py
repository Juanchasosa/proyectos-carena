from colorama import Back, Fore, init
init(True)

texto = "Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo."

print("\n")
print(texto)
print("\n")


articulos = {
            "el": 0,
            "la": 0,
            "los": 0,
            "las": 0,
            "un": 0,
            "una": 0,
            "unos": 0,
            "unas" : 0
}

for palabra in articulos :

    indice = 0

    while True :
        buscar = texto.lower().find(" " + palabra + " ", indice)

        if buscar == -1 :
            print("La palabra", "", Back.WHITE + Fore.RED + palabra, "", "no se encontró")
            break

        else:
            print("Se encontró la palabra", "", Back.WHITE + Fore.RED + palabra, "", "en la posición ", buscar)
            articulos[palabra] += 1
            indice = buscar + 1

for clave, valor in articulos.items() :
    print("Cantidad de apariciones de la palabra", Fore.RED + clave, valor)
