class Personaje:
    def __init__(self, nombre, tipo, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.set_energia(energia)
        
    def get_energia(self):
        return self.__energia
    
    def set_energia(self, energia):
        self.__energia = energia

        if self.__energia > 100:
            self.__energia = 100

        elif self.__energia < 0:
            self.__energia = 0
        
    def realizar_mision(self):
            self.set_energia(self.get_energia() - 5)
            print(f"¡Misión realizada con éxito! \n Energía: {self.get_energia()} %")
        
    def descansar(self):
            self.set_energia(self.get_energia() + 5)
            print(f"\n¡Energía restaurada! \nEnergía: {self.get_energia()} %")
    
    def mostrar_informacion(self):
        print(f"\nInformación del personaje. \n1) Nombre: {self.nombre} \n2) Tipo: {self.tipo} \n3) Energía: {self.get_energia()} %")
    
def main():
        personaje = Personaje("Kaizen", "Protagonista", 90)
        personaje.mostrar_informacion()
        personaje.realizar_mision()
        personaje.get_energia()
        personaje.descansar()
        
        personaje2 = Personaje("Astarion", "Antagonista", 150)
        personaje2.mostrar_informacion()
        personaje2.realizar_mision()
        personaje2.get_energia()
        personaje2.descansar()
        
        personaje2 = Personaje("Varkon", "Antagonista", -20)
        personaje2.mostrar_informacion()
        personaje2.realizar_mision()
        personaje2.get_energia()
        personaje2.descansar()
main()