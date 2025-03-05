
import numpy as np
import matplotlib.pyplot as plt

def graficar(y1):
    plt.figure()
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.grid(True)
    plt.hist(y1)
    plt.show()

canicas = 3000
niveles=12
final=[]

for i in range(canicas):
    ruta=np.random.randint(2,size=niveles)
    # print(ruta)
    posicion=np.sum(ruta)
    # print(posicion)
    final.append(int(posicion))
# print(f"final: {final}")
graficar(final)





