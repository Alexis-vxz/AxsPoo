from Aventurero import Aventurero

class Arquero(Aventurero):
    def __init__(self, nombre, nivel, flechas):
        super().__init__(nombre, nivel)
        self.flechas = flechas
        
    def usar_habilidad(self):
        super().usar_habilidad()
        self.flechas -= 1
        print(f"{self.nombre} dispara una flecha!! le quedan {self.flechas}")