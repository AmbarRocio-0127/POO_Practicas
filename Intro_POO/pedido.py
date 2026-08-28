class Pedido:
    
    def __init__(self, Cliente, Producto, Precio):
        self.cliente = Cliente
        self.producto = Producto
        self.Precio = Precio
    
    def mostrar_resumen(self):
        print(f"\nCliente: {self.cliente}")
        print(f"Producto: {self.producto}")
        print(f"Precio: {self.Precio}")

pedido1 = Pedido("Andrea", "Jugo", 30)
pedido2 = Pedido("Julieta", "Empanada", 40)
 
pedido1.mostrar_resumen()  
pedido2.mostrar_resumen()