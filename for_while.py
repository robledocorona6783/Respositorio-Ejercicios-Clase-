# print("Impares menores a 10")
# x=1

# while x <= 10:
#     print(x)
#     x += 2

# factorial = 5
# valor= factorial
# contador = valor - 1

# while contador > 0:
#     valor*= contador
#     contador -= 1

# print("El factorial de ",factorial,"es ",valor)

for i in 1,2,3:
    print(i)

for i in range(3):
    print(i)

for i in ["a","b","c","d"]:
    print(i)

for i in "Hola Mundo":
    if i== "M":
        pass
    else:
        print(i)

for i in range(2,100):
    primo=True
    for j in range(2,i):
        if i==j:
            break
        elif i%j==0:
            primo=False        
        else:
            continue
    if primo == True:
        print(i, end= " ")
    
