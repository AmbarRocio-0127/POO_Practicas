"""Ejercicio 5 - Videojuego"""
"""
    Atributos:
    - Título
    - Precio (> 0)
    - Clasificación PEGI (3, 7, 12, 16, 18)
"""
class Videojuego:
    def __init__(self, titulo, precio, clasificacion):
        self.__titulo = titulo
        self.__precio = precio
        self.__clasificacion = clasificacion

    #getters
    def get_titulo(self):
       return self.__titulo
    
    def get_precio(self):
       return self.__precio
   
    def get_clasificacion(self):
        return self.__clasificacion
    
    #setters
    def set_titulo(self, titulo):
        self.__titulo = titulo
        
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else: print("Valor Inválido.")
    
    #validación de rangos por las edades para cada clasificación de videojuego
    def set_clasificacion(self, clasificacion):
        match clasificacion:
            case x if x >= 18:
                return self.__clasificacion
            case x if x >= 16:
                return self.__clasificacion
            case x if x >= 12:
                return self.__clasificacion
            case x if x >= 7:
                return self.__clasificacion
            case x if x >= 3:
                return self.__clasificacion
            case _:
                print("Valor Inválido.")