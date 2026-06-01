class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

    def clasificar_inversion(self):

        if self.saldo >= 100000:
            return "Inversionista Premium"

        elif self.saldo >= 50000:
            return "Inversionista Medio"

        else:
            return "Inversionista Básico"
