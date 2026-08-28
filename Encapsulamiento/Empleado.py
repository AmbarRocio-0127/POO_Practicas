"""Ejercicio 4 - Empleado"""
"""
    Atributos:
    - Nombre
    - Salario (> 0)
    - Horas trabajadas (0 - 240)
"""
class Empleado:

    def __init__(self, nombre, salario, horas):
        self.__nombre = nombre
        self.__salario = salario
        self.__horas = horas
    
    #getter  
    def get_nombre(self):
        return self.__nombre
    
    def get_salario(self):
        return self.__salario
    
    def get_horas(self):
        return self.__horas
    
    #setter
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else: print("Valor Inválido")
        
    def set_horas(self, horas):
        if 0 < horas <= 240:
            self.__horas = horas
        else: print("Valor Inválido. Contáctese con administración.")