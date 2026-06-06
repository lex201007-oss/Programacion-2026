class Cliente:

    def __init__(self, id_cliente, nombre, direccion, fecha_nac):

        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__direccion = direccion
        self.__fecha_nac = fecha_nac
        self.__cuentas = []

    def obtener_id(self):
        return self.__id_cliente

    def obtener_nombre(self):
        return self.__nombre

    def obtener_direccion(self):
        return self.__direccion

    def obtener_fecha_nac(self):
        return self.__fecha_nac

    def obtener_cuentas(self):
        return self.__cuentas

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def __str__(self):

        return f"""
ID: {self.__id_cliente}
Nombre: {self.__nombre}
Dirección: {self.__direccion}
Fecha Nacimiento: {self.__fecha_nac}
"""
