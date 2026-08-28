"""Ejercicio 3 - Vehículo"""
"""
    Atributos:
    - Marca
    - Modelo
    - Velocidad (0 - 220 km/h)
    - Combustible (0 - 100 litros)

    Validaciones:
    0 <= velocidad <= 220
    0 <= combustible <= 100
    """
class Vehiculo:
    def __init__(self, marca, modelo, velocidad, combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__combustible = combustible
    
    #getters
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_velocidad(self):
        return self.__velocidad
    
    def get_combustible(self):
        return self.__combustible
    
    #setters
    def set_marca(self, marca):
        self.__marca = marca
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
        
    def set_velocidad(self, velocidad):
        if 0 <= velocidad <= 220:
            self.__velocidad = velocidad
        else: print("Valor Inválido.")
        
    def set_combustible(self, combustible):
        if 0 <= combustible <= 100:
            self.__combustible = combustible
        else: print("Valor Inválido.")
        