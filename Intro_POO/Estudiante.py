class Estudiante:
    
    def __init__(self, Nombre, Programa, Semestre):
        self.nombre = Nombre
        self.programa = Programa
        self.semestre = Semestre
    
    def presentarse(self):
        print(f"\nHola, soy {self.nombre}. \nEstudio {self.programa}. \nEstoy en semestre {self.semestre}")

estudiante1 = Estudiante("Juan","Ingeniería de Sistemas", 4)
estudiante2 = Estudiante("Ana","Diseño Gráfico", 2)

estudiante1.presentarse()
estudiante2.presentarse()