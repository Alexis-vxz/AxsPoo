from Herramientas import Herramienta

class Arco(Herramienta):
    """Ataca mobs a distancia con flechas."""   
    # TODO: propiedad 'nombre' y método 'usar'
    pass
    
    def __init__(self, material, durabilidad, flechas):
        # Llamamos al constructor de Herramienta para material y durabilidad
        super().__init__(material, durabilidad)
        self.flechas = flechas
    
    @property
    def nombre(self):
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self.flechas > 0:
            self.flechas -= 1
            daño = self.calcular_daño()
            self.desgastar()
            return f"Usando el {self.nombre} de {self._material} para atacar {objetivo} (daño: {daño}). Flechas restantes: {self.flechas}"
        else:
            return "Sin flechas"