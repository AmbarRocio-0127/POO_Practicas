"""Ejercicio 10 - Celular (Nivel intermedio)"""
"""
    Atributos:
    - Marca
    - Modelo
    - Batería (0 - 100)
    - Volumen (0 - 100)
"""
class Celular:
    def __init__(self, marca, modelo, bateria, volumen):
        self.__marca = marca
        self.__modelo = modelo
        self.__bateria = bateria
        self.__volumen = volumen
        
    #getters
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_bateria(self):
        return self.__bateria
    
    def get_volumen(self):
        return self.__volumen
    
    #setters
    def set_marca(self, marca):
        self.__marca = marca
        
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def set_bateria(self, bateria):
        if 0 < bateria <= 100:
            self.__bateria = bateria
        else: print("Valor fuera del rango establecido.")
        
    def set_volumen(self, volumen):
        if 0 < volumen <= 100:
            self.__volumen = volumen
        else: print("Valor fuera del rango establecido.")