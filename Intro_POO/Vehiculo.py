class Vehiculo:
    def __init__(self, Modelo, Marca, Color):
        self.modelo = Modelo
        self.marca = Marca
        self.color = Color
    
    def encender(self):
        print(f"Vehículo: {self.modelo} {self.marca} {self.color} ¡Encendido!\n")
        
vehiculo1 = Vehiculo("Toyota", "Corolla", "Blanco")
vehiculo2 = Vehiculo("Mazda", "CX-5", "N/A")

vehiculo1.encender()
vehiculo2.encender()