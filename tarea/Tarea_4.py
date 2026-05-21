class Expresion:
    pass


class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self):
        return self.valor


# Clase intermedia
class OperacionBinaria(Expresion):
    def __init__(self, izquierda, derecha):

        # Conversión automática a Numero
        if not isinstance(izquierda, Expresion):
            izquierda = Numero(izquierda)

        if not isinstance(derecha, Expresion):
            derecha = Numero(derecha)

        self.izquierda = izquierda
        self.derecha = derecha


class Suma(OperacionBinaria):
    def evaluar(self):
        return self.izquierda.evaluar() + self.derecha.evaluar()


class Resta(OperacionBinaria):
    def evaluar(self):
        return self.izquierda.evaluar() - self.derecha.evaluar()


class Producto(OperacionBinaria):
    def evaluar(self):
        return self.izquierda.evaluar() * self.derecha.evaluar()


# Ejemplos
a = Suma(5, 3)
b = Resta(a, 2)
c = Producto(b, 4)

print(a.evaluar())  # 8
print(b.evaluar())  # 6
print(c.evaluar())  # 24
