from colorama import Fore, init
init(True)

texto = "Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Spotify, Panda3D, entre otros."

textoList = texto.split()

print("==========================================================================================================================================")
print("\n")

for palabra in textoList :
    if palabra.istitle() :
        print(Fore.RED + palabra + " ", end='')
    else :
        print(Fore.GREEN + palabra + " ", end='')

print("\n")
print("==========================================================================================================================================")
