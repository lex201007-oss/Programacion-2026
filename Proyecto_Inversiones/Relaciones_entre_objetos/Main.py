from Cliente import Cliente
from Cuenta import Cuenta

cliente = Cliente("Alexander")

cuenta = Cuenta("INV001", cliente)

print(cuenta.numero)
print(cuenta.cliente.nombre)
