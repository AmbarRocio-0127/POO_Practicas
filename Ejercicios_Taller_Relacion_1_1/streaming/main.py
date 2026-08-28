from director import Director
from pelicula import Pelicula

director1 = Director("Joe Russo","Estadounidense", 14, True)
pelicula1 = Pelicula("Avengers: EndGame", "superhéroes, acción, ciencia ficción y aventura", "03:01:00", director1)
pelicula1.mostrar_pelicula()

#probando valores incorrectos
director1 = Director("Anthony Russo","Estadounidense", -1, True)