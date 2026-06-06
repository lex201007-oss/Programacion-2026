from Cuenta import Cuenta

class Cuenta_Inversion(Cuenta):

    def __init__(self, id_cuenta, saldo, rendimiento):
        super().__init__(id_cuenta, saldo)
        self.__rendimiento = rendimiento

    def obtener_rendimiento(self):
        return self.__rendimiento

    def obtener_tipo(self):
        return "Inversion"
