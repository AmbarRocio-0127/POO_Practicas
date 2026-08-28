class Videojuego:
    
    def __init__(self, Nombre, Categoria, Precio):
        self.nombre = Nombre
        self.categoria = Categoria
        self.precio = Precio
    
    def iniciar(self):
        print(f"\n¡Videojuego {self.nombre} Iniciado! \nCategoria {self.categoria}. \nPrecio: {self.precio}")
        
videojuego1 = Videojuego("Mario Bros", "Plataformas", 15000)
videojuego2 = Videojuego("Minecraft", "mundo abierto y género sandbox (caja de arena)", 25000)

videojuego1.iniciar()
videojuego2.iniciar()