#@author:Alexander  Inversion.py
class Inversion:
  #este es el método constructor que inicializa
  #a los atributos de una clase
  
  def __init__(self, valor1, valor2, valor3, valor4):
    self.saldo = valor1
    self.rendimiento = valor2
    self.tiempo = valor3
    self.empresa = valor4
  
 # Aumentar saldo
  def depositar(self, cantidad):
    self.saldo=self.saldo + cantidad
  
 # Disminuir saldo
  def retirar(self, cantidad):
    self.saldo=self.saldo - cantidad
 
#metodo que calcula la ganancia final de la inversion
  
  def calcular(self):
    monto = self.capital * (1 + self.rendimiento * self.tiempo)

  #mostrar los datos de la inversion
  def mostrar(self):
       print("Nombre de ka empresa:", self.empresa)
        print("Saldo actual:", self.saldo)
        print("Rendimiento:", self.Rendimiento)
        print("Tiempo:", self.tiempo, "meses")
