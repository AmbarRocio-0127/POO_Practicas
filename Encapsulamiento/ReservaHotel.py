"""Ejercicio 6 - ReservaHotel"""
"""
    Atributos:
    - Cliente
    - Huéspedes (1 - 6)
    - Noches (1 - 30)
"""
class ReservaHotel:
    def __init__(self, cliente, huespedes, noches):
        self.__cliente = cliente
        self.__huespedes = huespedes
        self.__noches = noches
    
    #getters    
    def get_cliente(self):
        return self.__cliente 

    def get_huespedes(self):
        return self.__huespedes
    
    def get_noches(self):
        return self.__noches
    
    #setters
    def set_cliente(self, cliente):
        self.__cliente = cliente 
    
    def set_huespedes(self, huespedes):
        if 0 < huespedes <= 6:
            self.__huespedes = huespedes
        else: print("Cantidad no permitida. Contacte la administración.")
    
    def set_noches(self, noches):
        if 1 < noches <= 30:
            self.__noches = noches
        else: print("La información solicitada no está disponible.")