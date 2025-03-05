
lista=[]

alumnos=0
while alumnos<=10:
    opcion= input("Agregar alumno(1) o salir(2) ")
    if opcion=="1":
        nombre=input("Agregue el nombre del Alumno ").capitalize()
        calificacion1=int(input(f'Ingrese la primer calificación de {nombre}: '))
        calificacion2=int(input(f'Ingrese la segunda calificación de {nombre}: '))
        calificacion3=int(input(f'Ingrese la tercer calificación de {nombre}: '))
        promedio=(calificacion1+calificacion2+calificacion3)/3
        alumno=[nombre,calificacion1,calificacion2,calificacion3,promedio]
        lista.append(alumno)
        alumnos+=1
    elif opcion=="2":
        print("El programa ha salido con ",alumnos," alumnos registrados")
        break
    else:
        print("Se ha ingresado una opción no valida")
        continue
print("La lista de alumnos es: ")

for i in range(len(lista)): 
    print(lista[i])