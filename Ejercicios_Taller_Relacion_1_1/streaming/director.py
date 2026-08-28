class Director:
    def __init__(self, nombre, nacionalidad, premios, esta_activo):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.__premios_obtenidos = 0
        self.set_premios_obtenidos(premios)
        self.esta_activo = esta_activo
    
    def get_premios_obtenidos(self):
        return self.__premios_obtenidos
    
    def set_premios_obtenidos(self, premios):
        if premios >= 0:
            self.__premios_obtenidos += premios
        elif premios < 0:
            print("Valor Inválido. Ingrese una cantidad correcta.")
    
    def mostrar(self):
        print("\n-----Director-----")
        print(f"\n1. Nombre: {self.nombre} \n2. Nacionalidad: {self.nacionalidad} \n3. Premios Obtenidos: {self.get_premios_obtenidos()} \n 4. Estado: {self.esta_activo}")