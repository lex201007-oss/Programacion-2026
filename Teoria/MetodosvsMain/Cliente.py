class Cliente:

    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def __str__(self):
        return "Cliente: " + self.nombre + " | " + str(self.cuenta)
