# numerador=10
# denominador=0
# cadena="3"
# numerico=5

# try:
#     print(numerador/denominador) #ZeroDivisionError: division by zero
# except ZeroDivisionError:
#     print("Ha ocurrido una división entre 0")    
# try:
#     print(cadena + numerico) #TypeError: can only concatenate str (not "int") to str
# except (ZeroDivisionError,TypeError):
#     print("Hay un error de concatenación")

# print("Fin del programa")

# while True:
#     try:
#         dividendo= int(input("Ingrese el dividendo: "))
#         divisor= int(input("Ingrese el divisor: "))
#         print("El resultado es:", dividendo/divisor)
#         break
#     except ValueError:
#         print("Debe ingresar un numero")
#     except ZeroDivisionError:
#         print("No se puede dividir entre 0")

# print("Fin del programa")

while True:
    nombre=input("Introduce tu nombre: ")
    apellido=input("Introduce tu apellido ")
    if nombre=="":
        print("No haz introducido tu apellido")
    elif apellido=="":
        print("No haz introducido tu apellido")
    else:
        break
while True:
    try:
        edad= int(input("Introduce tu edad "))
        break
    except ValueError:
        print("Debes introducir un numero")

correo=input("Introduce tu correo ")

while True:
    try:
        telefono= input("Introduce tu telefono ")
        int(telefono)
        break
    except ValueError:
        print("Debes introducir un numero")

print("Nombre: "+ nombre.capitalize())
print("Apellido: "+ apellido.capitalize())
print("Tengo: "+ str(edad)+ " años")
print("Correo: "+ correo)
print("Telefono: "+ telefono.capitalize())