class Cuenta:

    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def mostrar(self):
        print(self.numero)
        print(self.saldo)
