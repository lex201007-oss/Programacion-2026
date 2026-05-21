# Diccionario de letras a puntos
letra_a_puntos = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

# Diccionario inverso de puntos a letras
puntos_a_letra = {
    4.0: "A",
    3.7: "A-",
    3.3: "B+",
    3.0: "B",
    2.7: "B-",
    2.3: "C+",
    2.0: "C",
    1.7: "C-",
    1.3: "D+",
    1.0: "D",
    0.0: "F"
}

while True:

    entrada = input("Ingrese una calificación (Enter para salir): ")

    # Terminar si la línea está vacía
    if entrada == "":
        break

    # Intentar convertir de puntos a letra
    try:
        puntos = float(entrada)

        if puntos in puntos_a_letra:
            print("Calificación con letra:", puntos_a_letra[puntos])
        else:
            print("Entrada no válida")

    # Si falla, intentar convertir de letra a puntos
    except:
        entrada = entrada.upper()

        if entrada in letra_a_puntos:
            print("Puntos de calificación:", letra_a_puntos[entrada])
        else:
            print("Entrada no válida")
