estatus=1
a1=0
a2=0
while (estatus == 1):
    aactual = input("Ingresa el año actual ")
    if aactual.isnumeric():
        a1=int(aactual)

        apasado=input("Introduzca otro año ")
        if apasado.isnumeric():
            a2=int(apasado)

            diferencia= a2-a1

            if a1==a2:
                print("Es el mismo año, intentemos otra vez")
                estatus=1

            elif diferencia == 1:
                print("Para llegar al %s falta solo 1 año." %(a2))

            elif diferencia == -1:
                print("Desde el %s solo ha pasado 1 año." %(a2))

            else:
                print('La diferencia de años entre {} y {} es de {} años'.format(a1, a2, diferencia))
            

            estatus=int(input("""Quiere correr este programa de nuevo?
1.Si
2.No 
"""))


        else:
            print("Introduzca un año valido")
            estatus=1


    else:
        print("Introduzca un año valido")
        estatus=1

else:
    print("Gracias, hasta luego")