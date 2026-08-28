class Smartphone:
    def __init__(self, marca, modelo, porcentaje_bateria):
        self.marca = marca
        self.modelo = modelo
        self.set_bateria(porcentaje_bateria)
        
    def get_bateria(self):
        return self.__porcentaje_bateria
    
    def set_bateria(self, bateria):
        self.__porcentaje_bateria = bateria
        
        if self.__porcentaje_bateria > 100:
            self.__porcentaje_bateria = 100
            
        elif self.__porcentaje_bateria < 0:
            self.__porcentaje_bateria = 0    
        
        
    def usar_aplicacion(self):
            self.set_bateria(self.get_bateria() -2) 
            print(f"\nAplicación en Uso \nBateria: {self.get_bateria()} %")
        
    def cargar(self):
            self.set_bateria(self.get_bateria() + 2)
            print(f"\n¡Cargando Batería!")
        
    def mostrar_info(self):
        print(f"\nEstado del Smartphone. \n1) Marca: {self.marca} \n2) Modelo: {self.modelo} \n3) Porcentaje de Batería: {self.get_bateria()} %")
    
def main():
        smartphone1 = Smartphone("Samsung", "Galaxy Z Fold7", 90)
        smartphone1.mostrar_info()
        smartphone1.usar_aplicacion()
        smartphone1.mostrar_info()
        smartphone1.cargar()
        
        smartphone2 = Smartphone("Samsung", "Galaxy S26 Ultra", 110)
        smartphone2.mostrar_info()
        smartphone2.usar_aplicacion()
        smartphone2.mostrar_info()
        smartphone2.cargar()
        
        smartphone2 = Smartphone("Samsung", "Galaxy A57 5G,", -9)
        smartphone2.mostrar_info()
        smartphone2.usar_aplicacion()
        smartphone2.mostrar_info()
        smartphone2.cargar()
        
main()