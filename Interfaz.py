import tkinter as tk
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from urllib.request import urlopen
import json
from pathlib import Path
from io import BytesIO

ruta=Path("Pokedex")
ruta.mkdir(parents=True,exist_ok=True)
pokemon=""
info = {
                    'Image' : "",
                    'Id' : "",
                    'Nombre' : "",
                    'Altura' : "",
                    'Experiencia Base' : "",
                    'Peso' : "",
                    'Especie' : "",
                    'Tipo' : "",
                    'Hp' : "",
                    'Ataque' : "",
                    'Defensa' : "",
                    'Ataque especial' : "",
                    'Defensa Especial' : "",
                    'Velocidad' : "",
                    'Movimientos' : ""
}
lista_movimientos=[]

def funcion_boton1():
    caja_texto.place(x=50, y=55)
    caja_texto.delete(0, tk.END) 
    boton3.place(x=280, y=55) 

def fallo():
    caja_texto.place(x=50, y=55) 
    caja_texto.insert(0,"El pokemon no fue encontrado o no tiene imagen")
    etiqueta_imagen.place_forget()

def funcion_boton3():
    etiqueta_imagen.place(x=100,y=100)
    pokemon=caja_texto.get()
    caja_texto.delete(0, tk.END)
    caja_texto.place_forget()
    boton3.place_forget() 
    url="https://pokeapi.co/api/v2/pokemon/" + pokemon
    respuesta= requests.get(url)

    if respuesta.status_code != 200:
            fallo()

    pokemon_info=respuesta.json()

    try:

        movimientos=pokemon_info["moves"]
        for i in range(int(len(movimientos))):
            movimiento=movimientos[i]["move"]["name"]
            lista_movimientos.append(movimiento)
        
        url_imagen=pokemon_info["sprites"]["front_default"]
        imagen_respuesta = requests.get(url_imagen)

        if imagen_respuesta.status_code == 200:
            imagen = Image.open(BytesIO(imagen_respuesta.content))
            imagen_redimensionada = imagen.resize((300, 300))
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

            etiqueta_imagen.config(image=imagen_tk)
            etiqueta_imagen.image = imagen_tk 

            # imagen_redimensionada = imagen_tk.resize((50, 50))
            # imagenn_tk = ImageTk.PhotoImage(imagen_redimensionada)
            # etiqueta_imagen = tk.Label(ventana, image=imagenn_tk)
            # etiqueta_imagen.place(x=150,y=200)
            
        else:
            fallo()

        info["Image"]=url_imagen
        info["Id"]=pokemon_info[ 'id' ]
        info["Nombre"]=pokemon_info[ 'name' ]
        info["Altura"]=pokemon_info[ 'height' ]
        info["Experiencia Base"]=pokemon_info[ 'base_experience' ]
        info["Peso"]=pokemon_info[ 'weight' ]
        info["Tipo"]=pokemon_info[ 'types' ][0][ 'type' ][ 'name' ]
        info["Especie"]=pokemon_info[ 'species' ][ 'name' ]
        info["Hp"]=pokemon_info["stats"][0]["base_stat"]
        info["Ataque"]=pokemon_info["stats"][1]["base_stat"]
        info["Defensa"]=pokemon_info["stats"][2]["base_stat"]
        info["Ataque especial"]=pokemon_info["stats"][3]["base_stat"]
        info["Defensa Especial"]=pokemon_info["stats"][4]["base_stat"]
        info["Velocidad"]=pokemon_info["stats"][5]["base_stat"]        
        info["Movimientos"]=lista_movimientos

        extension=f"Pokedex_{pokemon}.json"
        archivo= ruta/extension

        with open(archivo,"w") as Pokedex:
            json.dump(info,Pokedex,indent=4)

    except :
        fallo()

    movimientos=pokemon_info["moves"]
    for i in range(int(len(movimientos))):
        movimiento=movimientos[i]["move"]["name"]
        lista_movimientos.append(movimiento)

    
    

ventana = tk.Tk()
ventana.geometry("500x400") 
ventana.title("Proyecto")
ventana.resizable(False, False)
boton1 = tk.Button(ventana, text="Buscar Pokemon",command=funcion_boton1)
boton1.place(x=50, y=20) 
boton2 = tk.Button(ventana, text="Salir",command=exit)
boton2.place(x=160, y=20) 
caja_texto = tk.Entry(ventana, font=("Arial", 14))
caja_texto.place(x=50, y=55)
caja_texto.place_forget()
boton3 = tk.Button(ventana, text="Añadir Pokemon",command=funcion_boton3)
boton3.place(x=280, y=55)
boton3.place_forget() 
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.place(x=100,y=100)

ventana.mainloop()