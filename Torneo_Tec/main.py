from Competidor import Competidor
from Observador import Observador

Donato = Competidor("Donato", "154612", "Avanzado", 0, " Los Chamos")
print("--- Competidor ---")
print(Donato.mostrar_perfil())

Donato.ganar_puntos(50) 
print("Después de ganar puntos:")
print(Donato.mostrar_perfil())
Donato.perder_puntos(10)
print("Después de perder puntos:")
print(Donato.mostrar_perfil())

Maria = Observador("Maria", "54321", "Intermedio", 15, ["Vistas 1"])
print("\n--- Observador ---")
print(Maria.mostrar_perfil())
Maria.ver_partida("Vistas 2")
print("Después de ver una partida:")
print(Maria.mostrar_perfil())
Maria.eliminar_observacion("Vistas 1")
print("Después de eliminar una observación:")
print(Maria.mostrar_perfil())
