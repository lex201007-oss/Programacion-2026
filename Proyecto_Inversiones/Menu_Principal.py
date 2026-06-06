from Datos import Datos
from Cuenta_Ahorro import Cuenta_Ahorro
from Cuenta_Inversion import Cuenta_Inversion

class Menu_Principal:

    def __init__(self):

        self.sistema = Datos.cargar()

    def mostrar_menu_principal(self):

        while True:

            print("\n===== SISTEMA DE INVERSIONES =====")
            print("1. Nuevo Cliente")
            print("2. Administrar Cuentas")
            print("3. Mostrar Clientes")
            print("4. Guardar")
            print("5. Salir")

            opcion = input("Opción: ")

            if opcion == "1":

                nombre = input("Nombre: ")
                direccion = input("Dirección: ")
                fecha = input("Fecha Nacimiento: ")

                cliente = self.sistema.crear_cliente(
                    nombre,
                    direccion,
                    fecha
                )

                print(cliente)

            elif opcion == "2":

                id_cliente = int(
                    input("ID Cliente: ")
                )

                cliente = self.sistema.buscar_cliente(
                    id_cliente
                )

                if cliente:
                    self.menu_cuentas(cliente)

                else:
                    print("Cliente no encontrado")

            elif opcion == "3":

                for cliente in self.sistema.obtener_clientes():
                    print(cliente)

            elif opcion == "4":

                Datos.guardar(self.sistema)

                print("Información guardada")

            elif opcion == "5":

                Datos.guardar(self.sistema)

                break

    def menu_cuentas(self, cliente):

        while True:

            print("\n===== CUENTAS =====")
            print("1. Crear Cuenta Ahorro")
            print("2. Crear Cuenta Inversión")
            print("3. Mostrar Cuentas")
            print("4. Regresar")

            opcion = input("Opción: ")

            if opcion == "1":

                cuenta = Cuenta_Ahorro(
                    self.sistema.generar_id_cuenta(),
                    0,
                    5
                )

                cliente.agregar_cuenta(cuenta)

                print("Cuenta ahorro creada")

            elif opcion == "2":

                cuenta = Cuenta_Inversion(
                    self.sistema.generar_id_cuenta(),
                    0,
                    12
                )

                cliente.agregar_cuenta(cuenta)

                print("Cuenta inversión creada")

            elif opcion == "3":

                for cuenta in cliente.obtener_cuentas():

                    print(
                        "ID:",
                        cuenta.obtener_id(),
                        "| Tipo:",
                        cuenta.obtener_tipo(),
                        "| Saldo:",
                        cuenta.obtener_saldo()
                    )

            elif opcion == "4":
                break
