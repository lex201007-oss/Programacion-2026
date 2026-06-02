from Cliente import Cliente
from Cuenta import Cuenta

cliente = Cliente("Alexander")
cuenta = Cuenta(120000)

print(cliente.nombre)
print(cuenta.clasificar_inversion())
