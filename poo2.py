class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria("Ana", 100000)

cuenta.depositar(50000)
cuenta.retirar(1)


print(cuenta.consultar_saldo())
