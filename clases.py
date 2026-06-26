class Aventurero:
    def __init__(self,nombre,nivel):
        self.nombre = nombre
        self.nivel = nivel
    
    def mostrar(self):
        print(f"{self.nombre} tiene un nivel de {self.nivel}")

    def subirNivel(self):
        self.nivel += 1

sub = Aventurero("Subaru", 20)
emi = Aventurero("Emilia", 95)
rei = Aventurero("Reinhard", 100)
sub.mostrar()
emi.mostrar()
rei.mostrar()

sub.subirNivel()
sub.mostrar()