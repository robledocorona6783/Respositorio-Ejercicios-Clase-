import numpy as np

lista_mayor=[]
nueva=[]
def crear_lista(longitud):
    lista=[]
    for i in range(longitud):
        valor=input(f"Que desea agregar a la lista en la posición {i+1}? ")
        lista.append(valor)
    lista_mayor.append(lista) 

def imprimir_listas():
    print(f"La lista completa de elementos antes de borrar es: {lista_mayor}")

def eliminar_listas():

    if listas==1:
        print("No se puede eliminar de una sola lista")
    else:
        # a=np.array(lista_mayor)
        # print(np.unique(a))
        for i in range(listas):
            for j in len(lista_mayor[i][j]):
                nueva.append(lista_mayor[i][j])
        print(nueva)

listas=input("Cuantas listas desea crear? ")
if listas.isdigit():
    listas=int(listas)
    if listas <= 0 :
        print("No se puede correr programa")
        exit()
    else:
        longitud=[]
        for i in range(listas):
            lenght=input(f"De que longitud desea que sea la lista {i+1}? ")
            if lenght.isdigit():
                lenght=int(lenght)
                longitud.append(lenght)
                crear_lista(lenght)
            else:
                print("Longitud no valida")
                exit()
            
    imprimir_listas()
    eliminar_listas()
else:
    print("Cantidad no valida")
    exit()



    