class Persona:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.set_documento(documento)
        
    def get_documento(self):
        return self.__documento
    
    def set_documento(self, documento):
        self.__documento = documento
        
    def mostrar_informacion(self):
        print(f"\nNombre: {self.nombre} \nDocumento: {self.get_documento()}")
        
class Docente(Persona):
    def __init__(self, nombre, documento, profesion):
        super().__init__(nombre, documento)
        self.profesion = profesion

class Estudiante(Persona):
    def __init__(self, nombre, documento, semestre):
        super().__init__(nombre, documento)
        self.semestre = semestre
        
def main():
    docente = Docente("Juliana Mendoza", 7125489632, "Maestra de Artes")
    estudiante = Estudiante("Amanda Mena", 215478963, 6)
    
    estudiante.mostrar_informacion()
    docente.mostrar_informacion()    
    
main()

"""
Reflexión

¿Qué ventajas obtuvo al utilizar herencia?"""
#Permitio reutilizar el codigo de la funcion de la clase padre. Lo cual hizo que fuera mas comodo 
# y mas entendible a la hora de leer el codigo
"""¿Qué código no tuvo que repetir?"""
#El codigo de la funcion mostrar_informacion() y los atributos pertenecientes a la clase padre, 
# que seria los atributos generalizados de cada uuna de las entidades.

"""
        DIAGRAMA DE CLASE CORRESPONDIENTE A ESTE CASO
                 _____________
                |             |
                |   Persona   |
                |_____________|
                       ▲
             __________|___________
            |                      |
            |                      |
     _________________      _________________
    |                 |    |                 |
    |    Docente      |    |   Estudiante    |
    |_________________|    |_________________|
"""