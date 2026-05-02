from Jugador import Jugador

class Observador(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, observaciones):
        super().__init__(nombre, num_control, nivel, puntos)
        self.observaciones = observaciones

    def mostrar_perfil(self):
        return super().mostrar_perfil() + f", Observaciones: {self.observaciones}"

    def ver_partida(self, observacion):
        self.observaciones.append(observacion)

    def eliminar_observacion(self, observacion):
        if observacion in self.observaciones:
            self.observaciones.remove(observacion)

    def actualizar_observaciones(self, observaciones):
        self.observaciones.extend(observaciones)

