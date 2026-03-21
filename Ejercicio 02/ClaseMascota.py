class Mascota: 
    def __init__(self,nombre,tipo,edad,nivelFelicidad): 
        self.nombre = nombre 
        self.tipo = tipo 
        self.edad = edad 
        self.nivelFelicidad = nivelFelicidad 
     
    def alimentar(self): 
        self.nivelFelicidad = 10 
        if self.nivelFelicidad > 100: 
            self.nivelFelicidad = 100 
            print(f"{self.nombre} se alimento muy bien, su nivel de felicidad aumentó a:{self.nivelFelicidad}")

             
    def jugar(self): 
        self.nivelFelicidad = 20 
        if self.nivelFelicidad > 100: 
            self.nivelFelicidad = 100 
            print(f"{self.nombre} se diivirtió jugando, ahora su nivel de felicidad es: {self.nivelFelicidad}")

             
    def mostrarEstado(self): 
        return f"Nombre: {self.nombre}, tipo: {self.tipo}, felicidad: {self.nivelFelicidad}"
    
    def esFeliz(self):
        return self.nivelFelicidad > 70
    
mascota1 = Mascota("Tilin","Perro", 5, 45)
print(mascota1.mostrarEstado())
print("Es feliz?", mascota1.esFeliz())

mascota1.alimentar()
print(mascota1.mostrarEstado()) 

mascota1.jugar() 
print(mascota1.mostrarEstado()) 
print("¿Es feliz?", mascota1.esFeliz()) 

mascota2 = Mascota("Michi", "Gato", 3, 85) 
print(mascota2.mostrarEstado()) 
print("¿Es feliz?", mascota2.esFeliz()) 

mascota2.alimentar() 
print(mascota2.mostrarEstado()) 

mascota2.jugar() 
print(mascota2.mostrarEstado()) 
print("¿Es feliz?", mascota2.esFeliz())