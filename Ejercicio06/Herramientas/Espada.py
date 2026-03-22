from Herramientas import Herramienta

class Espada(Herramienta):
    """Ataca mobs causando daño."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    @property
    def nombre(self) -> str:
        return "Espada"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usando el {self.nombre} de {self._material} para atacar {objetivo} (daño: {daño})"
    