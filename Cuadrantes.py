while True:

    x=int(input("Ingrese un numero para X, positivo o negativo ")) ##Pide numero para x
    y=int(input("Ingrese un numero para Y, positivo o negativo ")) ##Pide numero para y
    print("Determinando cuadrante.....................")

    if x>0 and y>0:
        print("Su coordenada se encuentra en el cuadrante 1")  ##Determina en que cuadrantes esta

    elif x>0 and y<0:
        print("Su coordenada se encuentra en el cuadrante 4")

    elif x<0 and y>0:
        print("Su coordenada se encuentra en el cuadrante 2")

    elif x<0 and y<0:
        print("Su coordenada se encuentra en el cuadrante 3")

    elif x==0 and y>0:
        print("Su coordenada se encuentra en el Eje Y positivo")

    elif x==0 and y<0:
        print("Su coordenada se encuentra en el Eje Y negativo")

    elif x>0 and y==0:
        print("Su coordenada se encuentra en el Eje X positivo")

    elif x<0 and y==0:
        print("Su coordenada se encuentra en el Eje X negativo")

    else:
        print("Su coordenada se encuentra en el Origen")

    opcion=input("Desea correr el programa de nuevo? (1) si (2) no ")
    if opcion=="1":
        continue
    else:
        print("Hasta luego")
        exit()
