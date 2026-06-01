class Cuenta:

    def __init__(self, saldo):
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo
