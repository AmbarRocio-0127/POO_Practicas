"""Ejercicio 2 - Estudiante"""
"""
    Atributos:
    - Nombre
    - Edad (entre 5 y 100 años)
    - Promedio (entre 0 y 5)

    Edad y promedio son sensibles.

    Tarea:
    - Crear constructor.
    - Crear getters.
    - Crear setters.
    - Validar los rangos.
"""
class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.__nombre = nombre
        self.__edad = edad
        self.__promedio = promedio
    
    # getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_promedio(self):
        return self.__promedio
    
    # setters
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_edad(self, edad):
        if edad >= 5 and edad <= 100:
            self.__edad = edad
        else: print("Edad no permitida para inscripción.")
    
    def set_promedio(self, promedio):
        if promedio >= 4.0 and promedio <= 5.0:
            self.__promedio = promedio
        elif promedio >= 2.0 and promedio <= 3.9:
            self.__promedio = promedio
        elif promedio >= 0 and promedio <= 1.9:
            self.__promedio = promedio
        else: print("Valor Inválido.")
            