import matplotlib.pyplot as plt

def diagrama_barras_calificaciones(inicio,final,color,ventas):
    """
    Dibujar la gráfica de barras con las ventas
    """
    plt.bar(ventas.keys(), ventas.values(),color=color)
    plt.title(f"Ventas de años {inicio} a {final}: " )


ventas=[]

ventas1= int(input("Con que año le gustaría iniciar el rango? "))
ventas2= int(input("Con que año le gustaría terminar el rango? "))
for i in range((ventas2-ventas1)+1):
    años=int(input(f"Cuanto vendió en el año {ventas1+i} "))
    ventas.append([ventas1+i,años])

ventas=dict(ventas)
diagrama_barras_calificaciones(ventas1, ventas2,"blue",ventas)
plt.show()

