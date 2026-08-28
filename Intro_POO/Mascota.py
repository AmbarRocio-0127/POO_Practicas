class Mascota:
    
    def __init__(self, Nombre, Especie, Edad):
        self.nombre = Nombre
        self.especie = Especie
        self.edad = Edad
    
    def saludar(self):
        print(f"\n¡Hola soy {self.nombre}! \nSoy de la raza {self.especie}. \nTengo {self.edad} años.")
        
mascota1 = Mascota("Toby", "Husky", 3)
mascota2 = Mascota("Candy", "chihuahua", 4)

mascota1.saludar()
mascota2.saludar()