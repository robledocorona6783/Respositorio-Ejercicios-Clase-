# A diferencia de las listas las tuplas son elemento inmutables

vocales=("a","e","i","o","u")
print(vocales[2])
print(vocales[:3] +vocales[2:])

print(vocales.index("o"))

lista_vocales= list(vocales) #convierte de tupla a lista
lista_vocales[2]="I"

print(lista_vocales)

tupla_vocales= tuple(lista_vocales)

