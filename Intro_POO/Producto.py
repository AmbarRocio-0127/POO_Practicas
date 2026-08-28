class Producto:
    def __init__(self, Nombre, Precio, Stock):
        self.nombre = Nombre
        self.precio = Precio
        self.stock = Stock
    
    def mostrar_detalle(self):
        print("========================")
        print("Información del Producto")
        print("========================")
        print(f"Nombre: {self.nombre} \nPrecio: {self.precio} \nStock: {self.stock}\n")
        
producto1 = Producto("Plátano", 15, 30)
producto2 = Producto("Leche", 20, 50)

producto1.mostrar_detalle()
producto2.mostrar_detalle()