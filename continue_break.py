# la sentencia break interrumpe la ejecución de un ciclo
# interrume una iteración y brinca a la siguiente iteración

for numero in range(1,11):
    if numero%2 ==1:
        continue
    else:
        print(numero,"es par")

numero=0

while numero < 11:
    numero+=1
    if numero%2==0:
        continue
    else:
        print(numero,"es impar")   

numero=int(input("Ingrese un dígito "))
limite_inferior=0
limite_superior=10
buscado=5
intentos=0

while True:
    intentos+=1
    if numero==buscado:
        print("El numero",numero,"fue encontrado en",intentos,"intentos")
        break
    elif numero<buscado:
        limite_superior=buscado
        buscado=(buscado+limite_inferior)//2
    else:
        limite_inferior=buscado
        buscado=(buscado+limite_superior)//2

print("Fin del programa")

numero=int(input("Ingrese un dígito "))
limite_inferior=0
limite_superior=10
buscado=5
intentos=0

while True:
    intentos+=1
    if numero==buscado:
        print("El numero",numero,"fue encontrado en",intentos,"intentos")
        exit()
    elif numero<buscado:
        limite_superior=buscado
        buscado=(buscado+limite_inferior)//2
    else:
        limite_inferior=buscado
        buscado=(buscado+limite_superior)//2

print("Fin del programa")

