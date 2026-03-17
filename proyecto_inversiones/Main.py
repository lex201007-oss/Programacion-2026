from Inversion import *
from Menu import *

menu = Menu("Bienvenido a Inversiones Lex")

inversion1 = Inversion(3000, 4.5, 24, "Apple")

menu.bienvenida()

while True:

    opcion = menu.opciones()

    if opcion == "1":
        cantidad = float(input("Cantidad a depositar: "))
        inversion1.depositar(cantidad)
        print("Capital actualizado:", inversion1.capital)

    elif opcion == "2":
        cantidad = float(input("Cantidad a retirar: "))
        inversion1.retirar(cantidad)
        print("Capital actualizado:", inversion1.capital)

    elif opcion == "3":
        resultado = inversion1.calcular()
        print("Monto final de la inversion:", resultado)

    elif opcion == "4":
        inversion1.mostrar()

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida")
