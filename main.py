from Personajes import *
from combate import batalla
from guardar import crearArchivo, recuperar

try:
    personajes = recuperar()

except FileNotFoundError:

    personajes = [
        Guerrero("Guts",100),
        Mago("Harry",70),
        Arquero("Legolas",60)
    ]

    crearArchivo(personajes)
personajes = recuperar()
while True: 
    print("--- Menu RPG---")
    print("1. Ver Personajes")
    print("2. Empezar Batalla")
    print("3. Empezar desde cero")
    print("4. guardar")
    print("5. salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        
        print("personajes cargados")
        for p in personajes:
            
            p.mostrar()
    elif opcion ==2:
        batalla(personajes)
        for p in personajes:
            if p.vida > 0:
                print(f"{p.nombre}")
        
    elif opcion ==3:
        personajes = recuperar()
        for p in personajes:
            p.vida = p.vidaMax
        crearArchivo(personajes)
    elif opcion ==4:
        crearArchivo(personajes)
    elif opcion == 5:
        print("Hasta la proxima: ")
        break

