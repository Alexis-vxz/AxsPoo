from Comida import Comida
from Bebida import Bebida
from Postre import Postre


Pollo_Empapelado = Comida("Pollo Empapelado", 150.00, "Saludable")
Pollo_Empapelado.mostrarInformacion()
Pollo_Empapelado.tipo()

Te_Verde = Bebida("Té Verde", 20, "Frio")
Te_Verde.mostrarInformacion()
Te_Verde.tipo()

Cheesecake = Postre("Cheesecake", 35.00, False)
Cheesecake.mostrarInformacion()
Cheesecake.tipo()