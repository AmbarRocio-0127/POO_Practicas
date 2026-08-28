"""Objetivo
Aprender a identificar correctamente qué información debe pertenecer a la clase padre.

Actividad 1
Complete la tabla: Información ¿Padre o hijo?

nombre                             | Padre
peso                               | Padre
cantidad de miembros en la manada  | Hijo
longitud de la trompa              | Hijo

Actividad 2
Escriba cuál será la clase padre."""
#La clase Animal

"""Actividad 3
Escriba cuáles serán las clases hijas."""
#Las clases León y Elefante.

"""Actividad 4
Implemente la solución en Python."""

class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        
class Leon(Animal):
    def __init__(self, nombre, peso, miembros_manada):
        super().__init__(nombre, peso)
        self.miembros_manada = miembros_manada
        
class Elefante(Animal):
    def __init__(self, nombre, peso, longitud_trompa):
        super().__init__(nombre, peso)
        self.longitud_trompa = longitud_trompa  