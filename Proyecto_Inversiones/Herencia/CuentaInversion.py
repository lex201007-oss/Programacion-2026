from Cuenta import Cuenta

class CuentaInversion(Cuenta):

    def __init__(self, numero, saldo, rendimiento):
        super().__init__(numero, saldo)
        self.rendimiento = rendimiento
