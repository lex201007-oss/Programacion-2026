from Cuenta import Cuenta

cuentas = []

cuentas.append(Cuenta("INV001", 50000))
cuentas.append(Cuenta("INV002", 80000))
cuentas.append(Cuenta("INV003", 120000))

for cuenta in cuentas:
    print(cuenta.numero, cuenta.saldo)
