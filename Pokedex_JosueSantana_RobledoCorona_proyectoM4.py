import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
from pathlib import Path
import os

ruta=Path("Pokedex")
ruta.mkdir(parents=True,exist_ok=True)

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

while True:
    opcion=input("Que desea hacer? 1-Añadir Pokemon Cualquier tecla-Salir ")
    if opcion == "1":
        pokemon=input("Escribe un pokemon ")
        url="https://pokeapi.co/api/v2/pokemon/" + pokemon
        respuesta= requests.get(url)

        if respuesta.status_code != 200:
            print("Pokemon no encontrado")
            exit()

        pokemon_info=respuesta.json()

        try:
            url_imagen=pokemon_info["sprites"]["front_default"]
            imagen=Image.open(urlopen(url_imagen))
        except :
            print("El pokemon no tiene imagen")

        movimientos=pokemon_info["moves"]
        for i in range(int(len(movimientos))):
            movimiento=movimientos[i]["move"]["name"]
            lista_movimientos.append(movimiento)

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

        plt.title(pokemon_info["name"])
        imgplot=plt.imshow(imagen)
        print(info)
        plt.axis('off')
        plt.show()

        extension=f"Pokedex_{pokemon}.json"
        archivo= ruta/extension

        with open(archivo,"w") as Pokedex:
            json.dump(info,Pokedex,indent=4)
    else:
        print("Buen día")
        exit()
