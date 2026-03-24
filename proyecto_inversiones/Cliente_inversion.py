class Cliente_inversion:

    # Constructor. Esta clase contiene tres atributos: nombre del cliente y cuenta de inversión
    def __init__(self, nombre, empresas, cuenta_inversion):
        self.nombre = nombre
        self.cuenta_inversion = cuenta_inversion

    def __str__(self):
        cadena = "\nNombre del cliente: " + self.nombre
        cadena += "\nCuenta de inversión: " + str(self.cuenta_inversion)
        return cadena
