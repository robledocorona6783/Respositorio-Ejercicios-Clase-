import string

def imprimir_letra(letra):
    abecedario = []
    for i in range(26):
        letra1 = chr(ord('a') + i)
        abecedario.append(letra1)
    for i in range(26):
        letra1 = chr(ord('A') + i)
        abecedario.append(letra1)
    indice_n = abecedario.index(letra)
    print(f"La letra siguiente de {letra} es {abecedario.__getitem__(indice_n + 1)}")



while True:
    letra=input("Introduzca una letra del abecedario, o presione 0 para salir ")
    if letra.isdigit():
        print("Introduzca un valor valido")
    else:
        if letra=="0":
            print("Fin del programa")
            break
            exit()
        else:
            imprimir_letra(letra)

