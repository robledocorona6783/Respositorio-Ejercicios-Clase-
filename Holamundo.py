# estatus=1
# while (estatus == 1):

#     print("Hola Mundo, este es mi primer programa del UCamp")
#     estatus=int(input("""Quiere correr este programa de nuevo?
#       1.Si
#       2.No 
#         """))
    

# else:
#     print("Gracias")
import numpy as np

x=[["a","b"],["a","c","b"]]
uniq = np.unique_all(x)
print(uniq.index)
