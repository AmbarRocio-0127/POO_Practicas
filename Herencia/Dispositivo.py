class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo}")
        
class Celular(Dispositivo):
     def __init__(self, marca, modelo, almacenamiento):
         super().__init__(marca, modelo)
         self.almacenamiento = almacenamiento
         
def main():
    dispositivo1 = Celular("Samsung", "Galaxy S26 Ultra", 68)
    dispositivo1.mostrar_info()
    
main()

"""Preguntas de reflexión"""

"""¿Qué ocurriría si no se llamara a super()?"""
# No se heredaria en la clase hija el constructor ni el metodo 
# correspondiente a la clase dispositivo que es la clase padre.
"""¿Qué atributos pertenecen al padre?"""
#Los atributos de marca y modelo son los correspondientes de la clase padre.
"""¿Cuál pertenece únicamente al hijo?"""
#El atributo almacenamiento es el que pertenece a la clase hija.