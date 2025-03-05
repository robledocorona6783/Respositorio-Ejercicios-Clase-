
# f_archivo=open("archivo1.txt","w")
# f_archivo.write("Este es mi primer archivo 1")
# f_archivo.close()

# f_lectura=open("archivo1.txt","r")
# f_lectura.close()

# print(f_archivo)
# print(f_lectura)

# f_lectura=open("archivo1.txt","r")
# print(f_lectura.closed)
# f_lectura.close()
# print(f_lectura.closed)

# with open("archivo1.txt","r") as f_lectura:
#     print(f_lectura.closed)
# print(f_lectura.closed)

# with open("archivo1.txt","a") as f_archivo: #a de append, agrega al final del archivo
#     f_archivo.write("\nEste es mi primer archivo 2")
#     f_archivo.write("\nEste es mi primer archivo 3")
#     f_archivo.write("\n")
#     f_archivo.write("\tEste es mi primer archivo 4")

# with open("archivo1.txt","r") as f_lectura: 
#     contenido=f_lectura.read()
#     print(f"****{contenido}****")
#     contenido=f_lectura.read()
#     print(f"****{contenido}****")

# with open("archivo1.txt","r") as f_lectura: 
#     num_lineas=0
#     for i in f_lectura:
#         num_lineas+=1
#         print(f"linea {num_lineas} : {i} ")
#     print(f"El archivo tiene {num_lineas} líneas")

# with open("archivo1.txt","r") as f_archivo: 
#     lista_lineas=f_archivo.readlines()
#     print(lista_lineas)
# # print(lista_lineas)

# lista_lineas[1]="Este es mi primer archivo"
# lista_lineas.insert(2,"Este es mi primer archivo")
# print(lista_lineas)

# with open("archivo1.txt","w") as f_archivo: 
#     f_archivo.writelines(lista_lineas)

while True:
    personas=[]
    print("""
        1.Agregar datos a la agenda
        2.Añadir al archivo         
          """)
    opcion=input("Seleccione una opción ")
    if opcion== "1":
        contacto=[]
        while True:
            nombre=input("Introduce tu nombre: ")
            apellido=input("Introduce tu apellido ")
            if nombre=="":
                print("No haz introducido tu apellido")
            elif apellido=="":
                print("No haz introducido tu apellido")
            else:
                contacto.append(nombre)
                contacto.append(apellido)
                break
        while True:
            try:
                edad= int(input("Introduce tu edad "))
                contacto.append(edad)
                break
            except ValueError:
                print("Debes introducir un numero")

        correo=input("Introduce tu correo ")
        contacto.append(correo)

        while True:
            try:
                telefono= input("Introduce tu telefono ")
                int(telefono)
                contacto.append(telefono)
                break
            except ValueError:
                print("Debes introducir un numero")
        personas.append(contacto)
    
    elif opcion== "2":
        with open("agenda.txt","w") as f_agenda:
            for persona in personas:
                f_agenda.write(f"{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n")
            print("Datos guardados en agenda")
            break
    else:
        print("Opción invalida, volver a intentarlo")