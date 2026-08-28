class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.set_edad(edad)
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
        
    def Presentarse(self):
        print(f"Nombre{self.nombre} \nEdad:{self.get_edad()}")
        
class Empleado(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
def main():
    empleado1 = Empleado("Juana", 25)
    empleado1.Presentarse()
    
main()

"""Preguntas de reflexión"""

"""¿La clase Empleado tiene constructor propio?"""
#El constructor propio que tiene pasa a ser el heredado de la clase persona, al este ser implementado pasa a ser de la misma.
#Cuenta con un constructor propio que reutiliza el de la clase persona.
"""¿De dónde obtiene el método presentarse()?"""
#Es heredado de la clase padre persona, y pasa a ser de la clase hija.
"""1) ¿Fue necesario volver a escribir ese método?"""
#No fue necesaria debido a que automaticamente la implementacion de la clase persona paso a ser de la clase empleado.