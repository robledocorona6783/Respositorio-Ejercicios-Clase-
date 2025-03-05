cuadrados=[]
for numero in range(10):
    numero= numero**2
    cuadrados.append(numero)
print(cuadrados)


cubos=[cubo **3 for cubo in range(10)]
print(cubos)

cubos = {numero : numero **3 for numero in range(10)}
print(cubos)

pares =[numero for numero in range(1,11) if numero%2==0]
impares =[numero for numero in range(1,11) if numero%2!=0]
print(pares,impares)

nombres= ["ana","fernando", "carlos","priscilla"]
print(nombres)
nombres=[nombre.capitalize() for nombre in nombres]
print(nombres)

