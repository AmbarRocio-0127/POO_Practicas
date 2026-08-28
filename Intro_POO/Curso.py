class Curso:
    def __init__(self, Nombre, Instructor, Duracion):
        self.nombre = Nombre
        self.instructor = Instructor
        self.duracion = Duracion
    
    def describir(self):
        print("========================")
        print("Información del Curso")
        print("========================")
        print(f"Nombre: {self.nombre} \nInstructor: {self.instructor} \nDuracion: {self.duracion}\n")
        
curso1 = Curso("Ana Rodriguez", "Pedro Santana", "4 Meses")
curso2 = Curso("Rubí Hernandez", "Juan Perez", "6 Meses")

curso1.describir()
curso2.describir()