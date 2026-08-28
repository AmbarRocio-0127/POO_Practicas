class Pelicula:
    def __init__(self, Nombre, Genero, Duracion):
        self.nombre = Nombre
        self.genero = Genero
        self.duracion = Duracion
        
    def reproducir(self):
        print(f"\nReproduciendo Película: {self.nombre}")

pelicula1 = Pelicula("Interestelar", "Ciencia Ficción", "2:49 (hh:mm)")
pelicula2 = Pelicula("Coco","Animación", "2:49 (hh:mm)")

pelicula1.reproducir()
pelicula2.reproducir()