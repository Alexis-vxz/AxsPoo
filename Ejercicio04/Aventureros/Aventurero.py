class Aventurero:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
    
    def presentarse(self):
        print(f"Hola soy : {self.nombre}, mi nivel actual es: {self.nivel}")
        
    def usar_habilidad(self):
        return Aventurero