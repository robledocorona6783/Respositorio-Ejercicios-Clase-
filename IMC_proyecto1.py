estatus=1
while (estatus == 1):    
    nombre = input("Escriba su Nombre: ")
    while (nombre == ""):
        nombre=input("Escriba su Nombre Por Favor: ")

    apellido_p = input("Introduzca su Apellido Paterno: ")
    while (apellido_p == ""):
        apellido_p=input("Escriba su Apellido Paterno Por Favor: ")

    apellido_m = input("Introduzca su Apellido Materno: ")
    while (apellido_m == ""):
        apellido_m=input("Escriba su Apellido Materno Por Favor: ")

    repeticion = True
    while(repeticion):
        edad = input("Introduzca su Edad: ")
        try:
            edad_r=int(edad)
            repeticion=False

            repeticion_1 = True
            while(repeticion_1):
                peso = input("Introduzca su Peso en Kilogramos: ")
                try:
                    peso_r=float(peso)
                    repeticion_1=False

                    repeticion_2 = True
                    while(repeticion_2):
                        estatura = input("Introduzca su Estatura en metros: ")
                        try:
                            estatura_r=float(estatura)
                            repeticion_2=False    


                            IMC= peso_r / (estatura_r*estatura_r)
                            # # IMC= float(input("Introduzca IMC "))
                            print("IMC: " + str(IMC) )  

                            if IMC > 0 and IMC < 18.9:
                                print("Peso Bajo")

                            if IMC > 18.9 and IMC < 24.99:
                                print("Peso Normal")

                            if IMC > 25 and IMC < 29.99:
                                print("Sobrepeso")

                            if IMC > 30 and IMC < 34.99:
                                print("Obesidad Leve")

                            if IMC > 35 and IMC < 39.99:
                                print("Obesidad Media")

                            if IMC > 40:
                                print("Obesidad Morbida")

                            estatus=int(input("""Quiere correr este programa de nuevo?
1.Si
2.No 
"""))
                        except  ValueError:
                            print("Escriba su Estatura Por Favor")

                except  ValueError:
                    print("Escriba su Peso Por Favor")

        except  ValueError:
            print("Escriba su Edad Por Favor")

else:
    print("Gracias, hasta luego")