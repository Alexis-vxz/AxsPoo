from Jugador import Jugador

class Competidor(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, equipo):
        super().__init__(nombre, num_control, nivel, puntos)
        self.equipo = equipo

    def mostrar_perfil(self):
        return super().mostrar_perfil() + f", Equipo: {self.equipo}"

    def ganar_puntos(self, puntos):
        self.puntos += puntos
        print(f"{self.nombre} ha ganado {puntos} puntos. Total de puntos: {self.puntos}")


    def perder_puntos(self, puntos):
        if self.puntos > 0:
            self.puntos -= puntos
            print(f"{self.nombre} ha perdido {puntos} puntos. Total de puntos: {self.puntos}")

    def actualizar_puntos(self, puntos):
        self.puntos += puntos
