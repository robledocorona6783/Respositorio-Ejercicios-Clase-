
lista1=[]
lista2=[]

def crear_lista(lon1,lon2):    
    for i in range(lon1):
        dato=input(f"Ingrese el dato {i+1} para la lista 1 ")
        lista1.append(dato)   
    for i in range(lon2):
        dato=input(f"Ingrese el dato {i+1} para la lista 2 ")
        lista2.append(dato)
    return lista1,lista2

def resta_lista(a,b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a


lon1=int(input("De que longitud quiere que sea la lista 1 "))
lon2=int(input("De que longitud quiere que sea la lista 2 "))
crear_lista(lon1,lon2)
print("----------------")
print("Listas originales")
print(lista1)
print(lista2)
print("----------------")
print("Los elementos de la lista 1 restando los elementos de la lista 2 es ")
print(resta_lista(lista1,lista2))
print("----------------")
