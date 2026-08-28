class Estudiante:
    def __init__(self, nombre_completo, curso, porcentaje_avance):
        self.nombre_completo = nombre_completo
        self.curso = curso
        self.set_avance(porcentaje_avance)
        
    def get_avance(self):
        return self.__porcentaje_avance
    
    def set_avance(self, avance):
        self.__porcentaje_avance = avance
        
        if self.__porcentaje_avance > 100:
             self.__porcentaje_avance = 100
             
        elif self.__porcentaje_avance < 0:
             self.__porcentaje_avance = 0
    
    def completar_actividad(self):
        self.set_avance(self.get_avance() + 2)
        print(f"Progreso Actual: {self.get_avance()} %")
    
    def mostrar_info(self):
        print(f"\nDatos del Estudiante \n1) Nombre Completo: {self.nombre_completo} \n2) Curso: {self.curso} \n3) Progreso Actual: {self.get_avance()} %\n")

def main():
    estudiante = Estudiante("Juliana Marte", "Python", 90)
    estudiante.mostrar_info()
    estudiante.completar_actividad()
    estudiante.completar_actividad()
    estudiante.completar_actividad()
    estudiante.completar_actividad()
    estudiante.mostrar_info()
    
    estudiante = Estudiante("Andrea Soriano", "Java", -5)
    estudiante.mostrar_info()
    estudiante.completar_actividad()
    estudiante.completar_actividad()
    estudiante.completar_actividad()
    estudiante.completar_actividad()
    estudiante.mostrar_info()

main()
    