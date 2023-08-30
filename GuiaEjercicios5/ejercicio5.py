from colorama import Back, Fore, init
init(True)

texto = "Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo."

print("\n")
print(texto)
print("\n")

nuevo_texto = texto.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")
print(nuevo_texto)

# for x in texto :

#     if x == "a" :
#         nuevo_texto = nuevo_texto + "1"
#     elif x == "e" :
#         nuevo_texto = nuevo_texto + "2"
#     elif x == "i" :
#         nuevo_texto = nuevo_texto + "3"
#     elif x == "o" :
#         nuevo_texto = nuevo_texto + "4"
#     elif x == "u" :
#         nuevo_texto = nuevo_texto + "5"
#     else:
#         nuevo_texto = nuevo_texto + x

# print(nuevo_texto)

