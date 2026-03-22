from Mob import Mob
class Creeper(Mob):
    """Mob agresivo, suena '...Ssssss', corre hacia el jugador."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self):
        return "...Ssssss"

    def comportamiento(self):
        return "agresivo"

    def moverse(self):
        return "corre hacia el jugador"

    def skill(self):
        return "detona al cargar cerca del jugador"