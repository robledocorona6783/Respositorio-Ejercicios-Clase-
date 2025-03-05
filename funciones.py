
# def funcion_simple():
#     """ Esta función no hace nada """
#     pass

# def saludo():
#     """ Función que saluda al mundo """
#     print("Hola Mundo")

# print("Antes de llamar funcion")
# funcion_simple()
# saludo()
# print("Despues de llamar funcion")
# help(saludo)
# help(funcion_simple)

#Probando ámbitos
# titulo= "Probando ámbitos"
# suma=10.5

# def sumar():
#     suma = 2+2
#     print("suma en ambito local ", str(suma), id(suma))

# print("Antes de llamar a la función sumar")
# print("Suma en ambito global",suma,id(suma))
# sumar()
# print("Despues de llamar a la función sumar")
# print("Suma en ambito global",suma,id(suma))

# def sumar(parametro1,parametro2):
#     print("Suma", parametro1+parametro2)

# argumento1=5
# argumento2=7

# sumar(argumento1,argumento2)
# sumar("Hola", "mundo")

##Parametros opcionales

# def muestra_alumno(nombre,edad=18,sexo="F"):
#     print(f"Nombre: {nombre}, edad: {edad}, sexo: {sexo}")

# muestra_alumno("Maria")#Obligatorio
# muestra_alumno("Maria",22)#Opcional
# muestra_alumno("Juan",sexo="M")#Opcional

def captura_alumnos(numero=3):
    lista_alumnos=[]
    for i in range(numero):
        nombre=input("Ingrese el nombre del alumno: ").capitalize()
        calificacion1= int(input(f"Ingrese la primera calificación de {nombre}: "))
        calificacion2= int(input(f"Ingrese la segunda calificación de {nombre}: "))
        lista_alumnos.append([nombre,calificacion1,calificacion2])
        promedio(nombre,calificacion1,calificacion2)
    print("Las calificaciones de los alumnos son: ",lista_alumnos)

def promedio(nombre,calificacion1,calificacion2):
    promedio=(calificacion1+calificacion2)/2
    print(f"El promedio de {nombre} es: {promedio}")


numero_alumnos=input("Cuantos alumnos desea registrar? ")

if numero_alumnos.isdigit():
    numero_alumnos= int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()