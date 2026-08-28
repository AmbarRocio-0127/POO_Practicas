class Mueble: 
    def __init__ (self, material, color):
        self.material = material
        self.color = color
    
    def describir(self):
        print(f"\nMaterial: {self.material} \nColor: {self.color}")
        
class Mesa(Mueble):
    def __init__(self, material, color, cantidad_patas):
        super().__init__(material, color)
        self.cantidad_patas = cantidad_patas

class Silla(Mueble):
    def __init__(self, material, color, tiene_espaldar):
         super().__init__(material, color)
         self.tiene_espaldar = tiene_espaldar
         
def main():
    mesa = Mesa("Mármol", "Negro Marquina", 4)
    silla = Silla("Tapiz Terciopelo", "Vino", True)
    mesa.describir()
    silla.describir()
    
main()

"""   DIAGRAMA CORRESPONDIENTE AL EJERCICIO IMPLEMENTADO
            (Clase Padre)
              Mueble
            ___________

           /           \\
          /             \\
        Mesa            Silla
       (Hija)           (Hija)
      _________      _________
"""