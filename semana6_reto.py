contra=0
contra2=0
cuenta=0
estatus =1
while estatus==1:

    contra= str(input("Introduzca una contraseña que empiece con un número por favor "))


    for i in range (len(contra)):
        if contra[0].isnumeric():
            terminal=1
            break
        else:
            terminal=2
            break

    while terminal == 2:
        print("La contraseña debe empezar con un número")
        estatus==1
        break

    while terminal ==1:
        contra2= str(input("Introduzca nuevamente la misma contraseña por favor ")) 
        if(contra==contra2):
            print("Contraseña correcta, fin del programa")
            exit()

        else:
            print("Contraseña incorrecta, intente nuevamente")
            cuenta +=1
            print(cuenta)
            terminal=1

            if cuenta >2:
                print("Demasiados intentos, fin del programa")
                exit()

