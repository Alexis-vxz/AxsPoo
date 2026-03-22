from Herramientas import Herramienta

class Pico(Herramienta):
    """Mina bloques de piedra, carbón, hierro, etc."""
    # TODO: propiedad 'nombre' y método 'usar'
    # En usar(): llama a calcular_daño() y a desgastar()
    pass

    @property
    def nombre(self) -> str:
        return "Pico"
    
    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usando el {self.nombre} de {self._material} para minar {objetivo} (daño: {daño})"  
    