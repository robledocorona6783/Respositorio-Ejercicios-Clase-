import requests

latitud=20.3001977
longitud=-103.261934

api_key="ae5cf1e1ced9c0d3cb26c84fa7969527"
url_destino=f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon{longitud}&lang=es&appid={api_key}"

respuesta= requests.get(url_destino,timeout=10)

if respuesta.status_code != 200:
    print("Ha ocurrido un error, intente nuevamente")
    exit()
else:
    print("Conexión exitosa")

datos=respuesta.json()
ciudad=respuesta["name"]
datos_clima=respuesta["weather"]
clima=datos_clima[0]["description"]

print(f"El clima en la ciudad: {ciudad} es: {clima}")


