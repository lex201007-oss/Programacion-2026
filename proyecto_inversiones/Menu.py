class Menu:

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def bienvenida(self):
        print(self.mensaje)

    def opciones(self):
        print("\nOpciones del sistema:")
        print("1. Depositar a la inversion")
        print("2. Retirar a la inversion")
        print("3. Calcular monto final")
        print("4. Mostrar datos")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")
        return opcion
