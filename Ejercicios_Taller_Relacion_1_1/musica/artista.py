class Artista:
    def __init__(self, nombre_artistico, pais, num_seguidores, cuenta_verificada):
        self.nombre_artistico = nombre_artistico
        self.pais = pais
        self.__num_seguidores = 0
        self.set_seguidores(num_seguidores)
        self.cuenta_verificada = cuenta_verificada  
    
    def get_seguidores(self):
        return self.__num_seguidores
    
    def set_seguidores(self, seguidores):
        if seguidores > 0:
            self.__num_seguidores += seguidores
        elif seguidores <= 0:
            print("\nValor no válido para el numero de seguidores.")
            
    def mostrar(self):
            print("\n-----Artista-----")
            print(f"\n1. Nombre Artistico: {self.nombre_artistico} \n2. País: {self.pais} \n3. Seguidores: {self.get_seguidores()} \n4. Estatus de la cuenta: {self.cuenta_verificada}")