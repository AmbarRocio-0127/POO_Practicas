class CuentaBancaria:
    def __init__(self, Titular, Saldo, Numero):
        self.titular = Titular
        self.saldo = Saldo
        self.numero = Numero
    
    def consultar_saldo(self):
        print(f"\nTitular: {self.titular}. \nSaldo: {self.saldo}. \nNúmero: {self.numero}")
        
cuenta1 = CuentaBancaria("Andrea Ramírez",500781.36, "00569874")
cuenta2 = CuentaBancaria("Pedro López", 456321.36, "00147897")

cuenta1.consultar_saldo()
cuenta2.consultar_saldo()