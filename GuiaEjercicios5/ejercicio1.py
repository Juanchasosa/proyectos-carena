from colorama import init, Style, Cursor, Back, Fore
init(True)

texto = "Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Spotify, Panda3D, entre otros."

print("=========================================================================================================================================")
print(texto)
print("=========================================================================================================================================")

while True :
    palabra = input("Ingrese la palabra que desea buscar en el texto: ")
    indice = texto.find(palabra)

    if palabra == "" :
        break

    if indice == -1 :
        print("La palabra no se encuentra")
    else:
        print("La palabra:", Fore.RED + palabra, "Se encuentra en el indice", indice)

print("Fin del programa")