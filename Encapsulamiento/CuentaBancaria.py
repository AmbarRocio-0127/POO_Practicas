"""Ejercicio 1 - Cuenta Bancaria (Muy fácil)"""
"""
    Atributos:
    - Titular: obligatorio
    - Saldo: nunca puede ser negativo (sensible)

    Tarea:
    1. Crear el constructor.
    2. Encapsular el saldo.
    3. Crear get_saldo().
    4. Crear set_saldo().
    5. Solo permitir valores mayores o iguales a cero.
"""
class CuentaBancaria:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo += saldo
        else: print("Valor inválido.")