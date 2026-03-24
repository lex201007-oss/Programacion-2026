from Cuenta import *
from Menu import *
from Cliente import *

class Main:
    pass


menu = Menu("Bienvenidos al Banco Pato")

menu.darBienvenida()
opcion = menu.despliegaMenu()


cuenta1 = Cuenta(300, "debito", "20/10/2007")

print("\nDatos de la cuenta:")
cuenta1.informacion()


if opcion == "1":
    cuenta1.depositar(800)
    print("\nDepósito realizado")
    cuenta1.informacion()

elif opcion == "2":
    cuenta1.retirar(100)
    print("\nRetiro realizado")

    cuenta1.infromacion()
