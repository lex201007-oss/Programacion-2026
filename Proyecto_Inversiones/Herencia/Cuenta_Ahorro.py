from Cuenta import Cuenta

class CuentaAhorro(Cuenta):

    def __init__(self, numero, saldo, interes):
        super().__init__(numero, saldo)
        self.interes = interes
