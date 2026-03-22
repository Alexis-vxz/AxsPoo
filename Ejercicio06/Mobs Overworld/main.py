# Generar las instancias para cada mob, y mostrar su sonido, comportamiento y forma de moverse.


from Vaca import Vaca

from Enderman import Enderman

from Creeper import Creeper

from Wither import Wither


if __name__ == "__main__":
    
    mobs = [
        Vaca("Vaca", 10),
        Creeper("Creeper", 20),
        Enderman("Enderman", 40),
        Wither("Wither", 100),
    ]
    for mob in mobs:
        mob.presentarse()

#Al instanciar Mob("test", 10) me marca error porque Mob es una clase abstracta y no se pueden crear objetos directamente de ella.