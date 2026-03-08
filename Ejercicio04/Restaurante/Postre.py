from Platillo import Platillo

class Postre(Platillo):
    def __init__(self, nombre, precio, es_con_mantequilla):
        super().__init__(nombre, precio)
        self.es_con_mantequilla = es_con_mantequilla
    
    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Contiene Mantequilla: {self.es_con_mantequilla}")
        
    def tipo(self):
        if self.es_con_mantequilla:
            return "Postre con Mantequilla"
        else:
            return "Postre sin Mantequilla"