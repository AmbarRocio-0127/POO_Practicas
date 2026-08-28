class Aire_Acondicionado:
    def __init__(self, marca, modelo, nivel_temperatura):
        self.marca = marca
        self.modelo = modelo
        self.set_temperatura(nivel_temperatura)
        
    def get_temperatura(self):
        return self.__nivel_temperatura
    
    def set_temperatura(self, temperatura):
        self.__nivel_temperatura = temperatura
        
        if self.__nivel_temperatura > 30:
            self.__nivel_temperatura = 30
            
        elif self.__nivel_temperatura < 16:
            self.__nivel_temperatura = 16
    
    def aumentar_temperatura(self):
        self.set_temperatura(self.get_temperatura() + 1)
        print(f"Temperatura Actual: {self.get_temperatura()}")
    
    def disminuir_temperatura(self):
        self.set_temperatura(self.get_temperatura() - 1)
        print(f"\nTemperatura Actual: {self.get_temperatura()}")
    
    def mostrar_informacion(self):
        print(f"\nInformación del Equipo. \n1) Marca: {self.marca} \n2) Modelo: {self.modelo} \n3) Temperatura Actual: {self.get_temperatura()} %")
    
def main():
        aire_acondicionado = Aire_Acondicionado("LG", "DualCool AI", 20)
        aire_acondicionado.mostrar_informacion()
        aire_acondicionado.aumentar_temperatura()
        aire_acondicionado.aumentar_temperatura()
        aire_acondicionado.aumentar_temperatura()
        aire_acondicionado.disminuir_temperatura()
        aire_acondicionado.mostrar_informacion()
        
        aire_acondicionado2 = Aire_Acondicionado("Samsung", "WindFree", 32)
        aire_acondicionado2.mostrar_informacion()
        aire_acondicionado2.aumentar_temperatura()
        aire_acondicionado2.aumentar_temperatura()
        aire_acondicionado2.aumentar_temperatura()
        aire_acondicionado2.disminuir_temperatura()
        aire_acondicionado2.mostrar_informacion()
        
        aire_acondicionado2 = Aire_Acondicionado("Daikin", "Perfera", 14)
        aire_acondicionado2.mostrar_informacion()
        aire_acondicionado2.aumentar_temperatura()
        aire_acondicionado2.aumentar_temperatura()
        aire_acondicionado2.aumentar_temperatura()
        aire_acondicionado2.disminuir_temperatura()
        aire_acondicionado2.mostrar_informacion()
main()