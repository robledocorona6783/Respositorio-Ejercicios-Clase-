import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
respuesta=requests.get(url,timeout=10)
try: 
    respuesta.status_code != 200
except requests.Timeout:
    print("Error: el tiempo de espera ha finalizado")

datos=respuesta.json()
nombre= datos["name"]
print(nombre)
movimientos=datos["moves"]
print("Movimientos de " + nombre + ": " )

for i in range(int(len(movimientos))):
    movimiento=movimientos[i]["move"]["name"]
    print(movimiento)
