     
"""Ejercicio 12 - Vuelo (Nivel avanzado)"""
"""
    Atributos:
    - Código
    - Capacidad (1 - 300)
    - Pasajeros registrados (0 - capacidad)

    Regla:
    Nunca puede haber más pasajeros que la capacidad.
"""
class Vuelo:
    def __init__(self, codigo, capacidad, pasajeros):
        self.__codigo = codigo
        self.__capacidad = capacidad
        self.__pasajeros = pasajeros
    
    #getters
    def get_codigo(self):
        return self.__codigo
    
    def get_capacidad(self):
        return self.__capacidad
    
    def get_pasajeros(self):
        return self.__pasajeros
    
    #setters
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_capacidad(self, capacidad):
        if 1 < capacidad <= 100:
            self.__capacidad = capacidad
        else: print("La capacidad excede el límite permitido. Por favor, ingrese un valor menor.")
    
    def get_pasajeros(self, pasajeros):
        if 0 < pasajeros <= self.__capacidad:
            self.__pasajeros = pasajeros
        elif pasajeros > self.__capacidad:
            print("La cantidad de pasajeros excede la capacidad máxima del avión.")
        else: print("Valor Inválido.")