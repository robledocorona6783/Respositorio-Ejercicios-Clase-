tiempos={
    "Hamilton": "1:49.8",
    "Bottas": "1:56.4",
    "Perez": "1:53.8",
    "HVertappen": "1:52.6"
}

print(tiempos.items())
print(tiempos.keys())
print(tiempos.values())
print(tiempos.get("Hamilton"))
print(tiempos.get("hamilton","No encontrado"))

tiempos1=dict(
   Hamilton= "1:49.8",
    Bottas= "1:56.4",
    Perez= "1:53.8",
    HVertappen= "1:52.6"
)

print(tiempos1)

##############################PILAS####################
# pila last in first out
# fila first in first out

pila = [3,6,7]

while len(pila) >= 3:
    if pila[-1] % 3:
        extraido=pila.pop()
        pila.append(extraido + 1)
    else:
        print("Todos los elementos de la lista son divisibles entre tres")
        break
