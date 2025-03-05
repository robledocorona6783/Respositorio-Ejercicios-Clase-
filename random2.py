import matplotlib.pyplot as plt

def diagrama_barras_calificaciones(notas,color,alumno):
    """
    Dibujar la gráfica de barras con las calificaciones
    """
    plt.bar(notas.keys(), notas.values(),color=color)
    plt.title("Calificaciones de : " + alumno)

calificaciones={
    "Programación":9,
    "Español":6.5,
    "Cálculo":4,
    "Historia":8,
    "Biología":10,
    "Ingles":3
    }
alumno=input("Nombre del alumno")
diagrama_barras_calificaciones(calificaciones,"blue",alumno)
plt.show()