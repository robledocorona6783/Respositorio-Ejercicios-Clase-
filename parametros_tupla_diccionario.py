
# def promedio(*numeros):
#     promedio= sum(numeros)/len(numeros)
#     print(f"El promedio es: {promedio}")

# promedio(4)
# promedio(4,5,6)
# promedio(1,2,3,4,5,6,7,8,9)


# def es_numero(titulo,*serie):
#     print(titulo)
#     for i in serie:
#         if type(i)==int or i.isdigit():
#             print(f"{i} es número")
#         else:
#             print(f"{i} no es número")

# # es_numero("Numeros","1","2","3")
# # es_numero("Letras","a","b","c")

# nombre= "Mezcla"
# lista_varios=["a","2",3,"f",5]
# es_numero(nombre, *lista_varios)

#Parámetros tipo diccionario

def area (**dato):
    if dato["figura"]=="Rectangulo":
        print(dato["base"]*dato["altura"])
    elif dato["figura"]=="Triangulo":
        print(dato["base"]*dato["altura"]/2)
    elif dato["figura"]=="Circulo":
        print(3.141593*dato["radio"]**2)
    else:
        print("Figura desconocida")

area(figura= "Triangulo",base=10, altura=5)
area(figura= "Circulo",radio=10, color="rojo")
area(figura= "Dodecagono",lado=10)