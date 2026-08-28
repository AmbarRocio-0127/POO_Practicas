"""Ejercicio 11 - Biblioteca (Nivel avanzado)"""
"""
    Atributos:
    - Título
    - Autor
    - Número de páginas (> 0)
    - Ejemplares disponibles (>= 0)
"""
class Libro:
    def __init__(self, titulo, autor, paginas, ejemplares):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
        self.__ejemplares = ejemplares
    
    #getters
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_paginas(self):
        return self.__paginas
    
    def get_ejemplares(self):
        return self.__ejemplares
    
    #setters
    def set_titulo(self, titulo):
        self.__titulo = titulo
        
    def set_autor(self, autor):
        self.__autor = autor
        
    def set_paginas(self, paginas):
        if paginas > 0:
            self.__paginas = paginas
        else: print("Valor Inválido")
        
    def set_ejemplares(self, ejemplares):
        if ejemplares >= 0:
            self.__ejemplares = ejemplares
        else: print("Valor Inválido")