from Cliente import Cliente

class Sistema_Inversiones:

    def __init__(self):

        self.__clientes = []

    def obtener_clientes(self):
        return self.__clientes

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def generar_id_cliente(self):
        return len(self.__clientes) + 1

    def generar_id_cuenta(self):

        total = 0

        for cliente in self.__clientes:
            total += len(cliente.obtener_cuentas())

        return total + 1

    def crear_cliente(
            self,
            nombre,
            direccion,
            fecha_nac):

        id_nuevo = self.generar_id_cliente()

        cliente = Cliente(
            id_nuevo,
            nombre,
            direccion,
            fecha_nac
        )

        self.agregar_cliente(cliente)

        return cliente

    def buscar_cliente(self, id_cliente):

        for cliente in self.__clientes:

            if cliente.obtener_id() == id_cliente:
                return cliente

        return None
