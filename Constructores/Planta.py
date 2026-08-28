class Planta:
    def __init__(self, nombre, tipo, nivel_agua):
        self.nombre = nombre
        self.tipo = tipo
        self.set_nivel_agua(nivel_agua)
        
    def get_nivel_agua(self):
        return self.__nivel_agua
    
    def set_nivel_agua(self, nivel_agua):
        self.__nivel_agua = nivel_agua
        
        if self.__nivel_agua > 100:
            self.__nivel_agua = 100
            
        elif self.__nivel_agua < 0:
            self.__nivel_agua = 0
    
    def regar(self):
            self.set_nivel_agua(self.get_nivel_agua() + 15)
            print(f"\nLa planta fue regada. {self.get_nivel_agua()} %")
            
    def pasar_dia(self):
            self.set_nivel_agua(self.get_nivel_agua() - 10)
            print(f"\nNivel de agua: {self.get_nivel_agua()} %")

    def mostrar_info(self):
        print("\nInformación de la planta")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de agua: {self.get_nivel_agua()} %")
    
def main():
        planta = Planta("Rosa", "Rosa", 60)
        planta.mostrar_info()
        planta.regar()
        planta.pasar_dia()
        planta.pasar_dia()
        planta.pasar_dia()
        planta.regar()
        planta.mostrar_info()
        
        planta = Planta("Orquídea", "Orquídea", 150)
        planta.mostrar_info()
        planta.regar()
        planta.pasar_dia()
        planta.pasar_dia()
        planta.pasar_dia()
        planta.regar()
        planta.mostrar_info()

        planta = Planta("Camelia", "Camelia", -5)
        planta.mostrar_info()
        planta.regar()
        planta.pasar_dia()
        planta.pasar_dia()
        planta.pasar_dia()
        planta.regar()
        planta.mostrar_info()
main()