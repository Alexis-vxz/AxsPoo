from Herramientas import Herramienta

class Pala(Herramienta):
    """Excava tierra, arena y grava rápidamente."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    @property
    def nombre(self) -> str:
        return "Pala"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usando el {self.nombre} de {self._material} para excavar {objetivo} (daño: {daño})"
