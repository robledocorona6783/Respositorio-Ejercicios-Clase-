diccionario_ingles={"rojo": "red","azul": "blue","negro": "black","cafe": "brown","amarillo": "yellow","naranja": "orange","verde": "green",}
diccionario_aleman={"rojo": "rot","azul": "blau","negro": "Schwarz","cafe": "braun","amarillo": "Gelb","naranja": "orange","verde": "Grün",}

frase= input("Ingrese una frase que tenga un color del arcoiris ")
frase=frase.lower()
palabras= frase.split()

menu= int(input("A que idioma quiere traducir? (1)Ingles (2)Aleman "))
respuesta=""

while True:
    if menu==1:
        for palabra in palabras:
            if palabra in diccionario_ingles.keys():
                respuesta= respuesta + diccionario_ingles[palabra] + " "
                serie=diccionario_ingles[palabra]         
            else:
                respuesta=respuesta + palabra + " "
                serie=""
        print("Tu color en ingles se dice",serie)
        break
                    
    elif menu==2:
        for palabra in palabras:
            if palabra in diccionario_aleman.keys():
                respuesta= respuesta + diccionario_aleman.get(palabra) + " " 
                serie=diccionario_aleman[palabra]                 
            else:
                respuesta=respuesta + palabra + " "
                serie=""
        print("Tu color en aleman se dice",serie) 
        break       
    else:
        print("Valor no valido")
        exit()

print(respuesta)