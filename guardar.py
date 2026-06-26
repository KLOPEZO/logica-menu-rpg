import json 
from Personajes import Guerrero, Mago, Arquero

def crearArchivo(personajes):
    datos = []
    for p in personajes:
        datos.append(p.guardar())

    
    with open("datos/partida.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def recuperar():
    with open("datos/partida.json", "r") as archivo:
     datos = json.load(archivo)

    personajes = []

    for p in datos:
        if p["tipo"] == "Guerrero":
            personaje = Guerrero(
                p["nombre"],
                p["vida"]
            )
            
        elif p["tipo"] == "Mago":
            personaje = Mago(
                p["nombre"],
                p["vida"]
            )

        elif p["tipo"] == "Arquero":
            personaje = Arquero(
                p["nombre"],
                p["vida"]
            )
        
        
        personaje.vidaMax = p.get("vidaMax", p["vida"])

        personajes.append(personaje)
    return personajes
    
