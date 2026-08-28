from artista import Artista
from cancion import Cancion 

def main():
    artista1 =  Artista("Juan Luis Guerra", "RD", 180001, True)
    cancion1 = Cancion("Las avispas", "03:17", 1000000, artista1)
    cancion1.mostrar_cancion()
    
    #probando valores incorrectos
    artista1 =  Artista("Juan Luis Guerra", "RD", -5, True)
main()