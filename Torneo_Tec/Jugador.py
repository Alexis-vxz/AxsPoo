class Jugador:
    def __init__(self, nombre, num_control, nivel, puntos):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = puntos

    def mostrar_perfil(self):
        return f"Nombre: {self.nombre}, Número de Control: {self.num_control}, Nivel: {self.nivel}, Puntos: {self.puntos}"

    def ganar_puntos(self, cantidad):
        self.puntos += cantidad
        print(f"{self.nombre} ha ganado {cantidad} puntos. Total de puntos: {self.puntos}")

    def perder_puntos(self, cantidad):
        self.puntos -= cantidad
        if self.puntos < 0:
            self.puntos = 0
            print(f"{self.nombre} ha perdido {cantidad} puntos. Total de puntos: {self.puntos}")

    def actualizar_puntos(self, puntos):
        self.puntos += puntos

