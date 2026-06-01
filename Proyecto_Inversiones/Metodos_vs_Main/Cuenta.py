class Cuenta:

    def __init__(self, capital, tasa):
        self.capital = capital
        self.tasa = tasa

    def calcular_rendimiento(self):
        return self.capital * self.tasa / 100
