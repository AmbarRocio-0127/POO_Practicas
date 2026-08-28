"""Ejercicio 8 - Curso"""
"""
    Atributos:
    - Nombre
    - Cupos disponibles (0 - 40)
    - Duración en horas (1 - 300)
    - Costo (> 0)
"""
class Curso:
    def __init__(self, nombre, cupos, horas, costo):
        self.__nombre = nombre
        self.__cupos = cupos
        self.__horas = horas
        self.__costo = costo
        
    #getters
    def get_nombre(self):
        return self.__nombre
    
    def get_cupos(self):
        return self.__cupos
    
    def get_horas(self):
        return self.__horas
    
    def get_costo(self):
        return self.__costo
    
    #setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_cupos(self, cupos):
        if 0 < cupos < 40:
            self.__cupos = cupos
        else: print("Cupos no disponibles")
    
    def set_horas(self, horas):
        if 1 < horas <= 300:
            self.__horas = horas
        else: print("Fuera del rango de horario disponible.")
        
    def set_costo(self, costo):
        if costo > 0:
            self.__costo = costo