"""Ejercicio 7 - Producto (Nivel intermedio)"""
"""
    Atributos:
    - Nombre
    - Precio (> 0)
    - Stock (>= 0)
    - Descuento (0 - 50%)
"""
class Producto:
    def __init__(self, nombre, precio, stock, descuento):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__descuento = descuento
      
      #getters  
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def get_stock(self):
        return self.__stock
    
    def get_descuento(self):
        return self.__descuento
    
    #setters
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def set_precio(self, precio):
        if precio > 0 :
            self.__precio = precio
        else: print("Valor Invalido.")
        
    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else: print("Valor Invalido.")
        
    def set_descuento(self, descuento):
        if 0 < descuento < 50:
            self.__descuento
        else: print("Valor Inválido.")