from Pico import Pico
from Espada import Espada
from Pala import Pala
from Arco import Arco

if __name__ == "__main__":
    herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
        Arco("Madera", 6, flechas=3)
    ]
    objetivos = ["mena de diamante", "Creeper", "arena", "esqueleto"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()
