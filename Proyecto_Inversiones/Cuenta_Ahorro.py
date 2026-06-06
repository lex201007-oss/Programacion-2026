from Cuenta import Cuenta

class Cuenta_Ahorro(Cuenta):

    def __init__(self, id_cuenta, saldo, interes):

        super().__init__(id_cuenta, saldo)

        self.__interes = interes

    def obtener_interes(self):
        return self.__interes

    def obtener_tipo(self):
        return "Ahorro"
