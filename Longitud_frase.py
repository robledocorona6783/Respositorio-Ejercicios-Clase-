while True:

    frase=input("Introduzca una palabra entre 4 y 8 letras ") ##Pide la palabra

    if len(frase) >= 4 and len(frase) <= 8:
        print("La palabra entra dentro de los parametros, tiene ",len(frase)," letras" ) ##Determina que la opción tiene entre 4 y 8 letras
        opcion=input("Desea correr el programa de nuevo? (1) si (2) no ")
        if opcion=="1":
            continue
        else:
            print("Hasta luego")
            exit()

    elif len(frase) <= 3:
        print("La palabra es muy corta, tiene ",len(frase)," letras ") ##Determina que la opción tiene menos de 4 letras
        opcion=input("Desea correr el programa de nuevo? (1) si (2) no ")
        if opcion=="1":
            continue
        else:
            print("Hasta luego")
            exit()

    else:
        print("La palabra es muy larga, tiene ",len(frase)," letras ") ##Determina que la opción tiene mas de 8 letras
        opcion=input("Desea correr el programa de nuevo? (1) si (2) no ")
        if opcion=="1":
            continue
        else:
            print("Hasta luego")
            exit()