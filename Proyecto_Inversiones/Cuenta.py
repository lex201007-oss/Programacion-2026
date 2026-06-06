class Cuenta:

    def __init__(self, id_cuenta, saldo):

        self.__id_cuenta = id_cuenta
        self.__saldo = saldo

    def obtener_id(self):
        return self.__id_cuenta

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):

        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True

        return False

    def obtener_tipo(self):
        return "General"
