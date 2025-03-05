entrada = input("Ingresa tu edad ")

edad=0

if entrada.isnumeric():
    edad=int(entrada)
else:
    print("Favor de introducir un numero")
    exit()

if edad <= 0:
    print("Introduzca edad valida")
elif edad >= 115:
    print("Dame consejos")
elif edad < 18:
    print("Eres menor de edad, vete antes de que le llame a tus padres")
else:
    print("Puedes comprar tus cigarrillos")