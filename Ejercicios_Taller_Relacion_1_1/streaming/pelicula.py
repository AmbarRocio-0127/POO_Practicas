from director import Director 

class Pelicula:
    def __init__(self, titulo, genero, duracion, director):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.director = director
        
    def mostrar_pelicula(self):
        print("\n-----Película-----")
        print(f"\n1. Título: {self.titulo} \n2. Género: {self.genero} \n3. Duración: {self.duracion}")
        self.director.mostrar()