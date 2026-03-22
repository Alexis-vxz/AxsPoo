from Mob import Mob

class Enderman(Mob):
    """Mob neutral, sonido distorsionado, se teletransporta."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self):
        return "Distorsionado"

    def comportamiento(self):
        return "Molesto si lo miras a los ojos"

    def moverse(self):
        return "se teletransporta"

    def skill(self):
        return "teletransportación rápida al ser atacado"