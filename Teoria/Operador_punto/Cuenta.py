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
  

