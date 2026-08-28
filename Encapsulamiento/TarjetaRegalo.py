"""Ejercicio 9 - Tarjeta de Regalo (Nivel intermedio)"""
"""
    Atributos:
    - Código
    - Saldo (>= 0)
    - Estado (ACTIVA o BLOQUEADA)
"""
class TarjetaRegalo:
    def __init__(self, codigo, saldo, estado):
        self.__codigo = codigo
        self.__saldo = saldo
        self.__estado = estado
    
    #getters
    def get_codigo(self):
        return self.__codigo
    
    def get_saldo(self):
        return self.__saldo
    
    def get_estado(self):
        return self.__estado
    
    #setters
    def set_codigo(self, codigo):
        self.__codigo = codigo
        
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else: print("Valor Inválido")
        
    def set_estado(self, estado):
        if estado == True:
            self.__estado = estado
        else: print("N/A")