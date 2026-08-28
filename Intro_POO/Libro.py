class Libro:
    def __init__(self, titulo, autor, cantidadpaginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidadpaginas
     
    def mostrar_informacion(self):
        print(f"\nTítulo del Libro:{self.titulo}")
        print(f"Autor del Libro:{self.autor}")
        print(f"Cantidad de páginas del Libro:{self.cantidad_paginas}\n")

libro1 = Libro("Cien años de Soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)

libro1.mostrar_informacion()
libro2.mostrar_informacion()