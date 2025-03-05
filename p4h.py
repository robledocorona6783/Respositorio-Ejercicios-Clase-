# # entero_var= 10
# # float_var= 2.5
# # string_var= "hola mundo"
# # float_text= str(float_var)

# # print(entero_var)
# # print(float_var)
# # print(string_var)
# # print(float_text)
# # print(type(string_var))
# # print(type(float_text))

# num=int(input("Introduce un número: "))
# if (num>0):
#     print("Número positivo")
# elif (num==0):
#     print("cero")
# else:
#     print("Número negativo")


# # comparar dos números

# num1= float(input("Introduce el primer número: "))
# num2= float(input("Introduce el segundo número: "))

# if(num1 == num2):
#     print("Los números son iguales")
# else:
#     print("Los números son distintos")

# for letra in "Hola Mundo":
#     print(letra)


# num= int(input("Escoge un número: "))
# for mult in range(11):
#     print(str(num) + "x" + str(mult) + "=" + str(num*mult))

# num= int(input("Ingrese un número: "))
# mult = 0 
# while (mult<11):
#     print(str(num),"x",str(mult),"=",str(num*mult))
#     mult+=1

# opcion=int(input("Introduzca un numero del 1 al 7 "))
# if opcion==1:
#     print("Su dia es Lunes")
# elif opcion==2:
#     print("Su dia es Martes")
# elif opcion==3:
#     print("Su dia es Miercoles")
# elif opcion==4:
#     print("Su dia es Jueves")
# elif opcion==5:
#     print("Su dia es Viernes")
# elif opcion==6:
#     print("Su dia es Sabado")
# elif opcion==7:
#     print("Su dia es Domingo")
# else:
#     print("Solo hay 7 días")

# edad=int(input("Cual es su edad? "))
# if edad >= 18 and edad <= 60:
#     print("Elegible hasta ahora")
#     exp=int(input("Tiene experiencia programando en python? 1) si tengo experiencia 2) no tengo experiencia pero si conocimiento "))
#     if exp==1:
#         print("Candidato elegible")
#         exit()
#     else:
#         print("Lo sentimos, no es lo que buscamos")
#         exit()

# else:
#     print("Lo sentimos, no cumple con nuestro rango")
#     exit()

# num=0
# suma=0
# while num <= 100:
#     suma=suma + num
#     num+=1
# print("""
#       El valor total es: """,suma,"")

# for i in range(2,50,2):
#     print(i)

# for i in range(1,51):
#     if i %2==0:
#         print(i)

# contra=input("Ingrese una contraseña ")
# while True:
#     val_contra=input("Vuelva a ingresar la contraseña ")
#     if contra == val_contra:
#         print("Las contraseñas coinciden")
#         break
#     else:
#         print("No coinciden, vuelva a intentar")
#         continue

# def mostrar_mensaje():
#     print("Hola mundo")
#     print("Adios mundo")

# def tabla_multiplicar(mult):
#     for mult in range(11):
#         print(str(mult) + "x" + str(mult) + "=" + str(mult*mult))

# def area_cuadrado(mult):
#         print("El area del cuadrado es " + str(mult*mult))

# mostrar_mensaje()
# tabla_multiplicar(8)
# area_cuadrado(10)

# nombres = ["Juan", "Sarah", "Maria", "Isabela"]
# # print(nombres[1])
# nombres.insert(3,"Ramon")
# nombres.append("Alex")
# nombres.remove("Sarah")
# del nombres[2]
# print(nombres[0:2])

# for i in nombres:
#     print(i)
# edades=[6,8,9,17,30]
# lista1=[nombres,edades]
# print(lista1)

# ###########################tupla

# nombres2=("Juan", "Sarah", "Maria", "Isabela")
# print(nombres2)
# nombres2=list(nombres2)
# nombres2=tuple(nombres2)

# def calcularmedia(*args): #args significa que le vamos a pasar un numero indeterminado de argumentos a nuestra función, se guardan como una tupla
#     total=0
#     for i in args:
#         total=total+i
#     resultado=total/2
#     print("La media es ", resultado)

# calcularmedia(10,10,9,6,4,7)


# def juego(numero_secreto, intentos):
#     numero_intentos = 1             
#     numero_usuario = int(input("Por favor introduce un número del 1 al 10: "))  
    
#     while (numero_secreto != numero_usuario) and (numero_intentos <= intentos):
#         if numero_secreto > numero_usuario:
#             print("El número secreto es mayor")
#         else:
#             print("El número secreto es menor")
#         numero_usuario = int(input("Por favor vuelve a introducir un número: "))
#         numero_intentos = numero_intentos + 1               
#         print("Número de intentos:", numero_intentos) 
#     return numero_intentos                        

# def resultados(numero_intentos, intentos):  
#     if numero_intentos <= intentos:        
#         print("""                *********
#                 WINNER            
#                 *********""")
#     else:
#         print("""                 *********"
#             "GAME OVER"         
#              "*********""")

# import random                           
# numero_secreto = random.randint(1, 10)  
# print(numero_secreto)                   
# intentos = 3                         
# numero_intentos = juego(numero_secreto, intentos)
# resultados(numero_intentos, intentos)

import random as rd
palabras=["capuchino", "café","perro","pelicula","galleta","botella","plato","arbol","navidad","balon","marciano"]
indice=rd.randint(0,len(palabras)-1)
secreta=palabras[indice].upper()
cadena= "-" * len(secreta) 
intentos_restantes=0
print(secreta)

while True:
    print(cadena)
    letra=input("Introduce una letra ").upper()
    if letra in secreta:
        for i in range(len(secreta)):
            if secreta[i] == letra:
                cadena = cadena[:i] + letra + cadena[i+1:]

    else:
        intentos_restantes+=1
        print("No es correcta, te quedan ", str(6-intentos_restantes)," intentos restantes")


        if intentos_restantes==6:
            print("Lo siento, haz perdido")
            break 

    if cadena==secreta:
        print("Haz ganado, felicidades") 
        break


# while intentos_restantes > 0 :

#     palusuario=input("Introduce una letra ").upper

#     for letra in letras_adivinadas:
#         if letra in letras:
#             tablero+=letra
#         else:
#             tablero+=""
#     print(tablero)

#     if letra in letras_adivinadas:
#         print("Ya haz introducido esa letra, prueba otra")

#     if letra in pal:
#         letras_adivinadas.append(letra)
#         if set(letras_adivinadas) == set(pal):
#             print("Ha ganado")
#             break
#         else:
#             intentos_restantes-=1
#             print("Incorrecto, le quedan ",str(intentos_restantes), " restantes.")
#     if intentos_restantes==0:
#         print("Ha perdido")







