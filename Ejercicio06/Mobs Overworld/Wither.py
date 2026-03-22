from Mob import Mob

class Wither(Mob):
    """Mob agresivo, suena 'Grrrr', vuela y dispara cabezas de esqueleto."""
        #Todo: implementa hacer_sonido, comportamiento, moverse

    def hacer_sonido(self):
        return "Grrrr"
    def comportamiento(self):
        return "agresivo"
    def moverse(self):
        return "vuela y dispara cabezas de esqueleto"
    def skill(self):
        return "invulnerabilidad temporal al recibir daño"
        