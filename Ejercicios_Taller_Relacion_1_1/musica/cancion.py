from artista import Artista
class Cancion:
    def __init__(self, titulo, duracion, reproducciones, artista):
        self.titulo = titulo
        self.duracion = duracion
        self.reproducciones = reproducciones
        self.artista = artista
        
    def mostrar_cancion(self):
        print("\n-----Canción-----")
        print(f"\n1. Titulo: {self.titulo} \n2. Duración: {self.duracion} \n3. Reproducciones: {self.reproducciones}")
        self.artista.mostrar()