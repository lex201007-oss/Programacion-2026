# Alexander  cuenta.py
class Cuenta:
  #este es el método constructor que inicializa
  #a los atributos de una clase
  def __init__(self, valor):
    self.saldo = valor

#Menu.py
#from Cuenta import
class Cuenta:
  
  def __init__(self, valor1, valor2, valor3):
    self.saldo = valor1
    self.tipo = valor2
    self.fechaCreacion = valor3
  
  def depositar(self, cantidad):
    self.saldo=self.saldo+cantidad
  
  def retirar(self, cantidad):
    self.saldo=self.saldo-cantidad
  
  def informacion(self):
    print("Saldo::", self.saldo)
    print("Tipo::", self.tipo)
    print("Fecha de creacion::", self.fechaCreacion)
    pass

class Menu:
  pass

print("Probando el objeto")
cuenta1 = Cuenta(3000, "Dèbito", "20/10/2007")
print( cuenta1.saldo)
print( cuenta1.tipo)
print( cuenta1.fechaCreacion)

cuenta1.depositar(5000)
print("probando el deposito")
print(cuenta1.saldo)

cuenta1.retirar(1200)
print("probando el retiro")
print(cuenta1.saldo)

cuenta2 = Cuenta(5000, "Crédito", "20/10/2007")
print("probando el objeto")
print(cuenta2.saldo)
print(cuenta2.tipo)
print(cuenta2.fechaCreacion)

cuenta1=  Cuenta(3000, "Dèbito", "20/10/2007")

cuenta1.informacion()
cuenta2=  Cuenta(5000, "Crédito", "20/10/2007")

cuenta2.informacion()
