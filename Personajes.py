import random
import json

class Personajes:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida 
        self.experiencia = 0 
        self.vidaMax = vida
    def mostrar(self):
        print(f"{self.nombre} tiene {self.vida} de vida")
    
    def recibirDaño (self, cantidad):
        if cantidad >= self.vida:
            self.vida = 0 
            print(f"El personaje {self.nombre} esta muerto")
        elif cantidad > 0 and cantidad< self.vida:
            self.vida -= cantidad
    def experienciaG (self, cantidad):
        self.experiencia += cantidad
    def guardar(self):
        return {
            "tipo": self.__class__.__name__,            
            "nombre": self.nombre,
            "vida" : self.vida
        }
    
class Guerrero(Personajes):
    def atacar(self, enemigo):
        enemigo.recibirDaño(15)
        print(f"{self.nombre} ataco a {enemigo.nombre}")
    

class Mago(Personajes):
    def atacar(self, enemigo):
        enemigo.recibirDaño(25)
        print(f"{self.nombre} Lanzo una bola de fuego a {enemigo.nombre}")

class Arquero(Personajes):
    def atacar(self, enemigo):
        enemigo.recibirDaño(10)
        print(f"{self.nombre} ataco a {enemigo.nombre}")


guts = Guerrero("Guts", 100)

harry = Mago("Harry", 70)
legolas = Arquero("Legolas", 60)




personajes = [guts, harry, legolas]

"""while harry.vida > 0 and guts.vida >0 and legolas > 0:
    guts.atacar(harry)

    if harry.vida > 0: 
        harry.atacar(guts)"""
    















     
