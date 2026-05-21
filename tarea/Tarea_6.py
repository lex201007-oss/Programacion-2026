import sys
import string

# Verificar que se proporcione el nombre del archivo
if len(sys.argv) != 2:
    print("Error: Debe proporcionar el nombre del archivo.")
    sys.exit()

nombre_archivo = sys.argv[1]

try:

    archivo = open(nombre_archivo, "r", encoding="utf-8")

    palabra_anterior = ""
    linea_anterior = 0

    numero_linea = 0

    for linea in archivo:

        numero_linea += 1

        # Eliminar signos de puntuación y convertir a minúsculas
        for signo in string.punctuation:
            linea = linea.replace(signo, " ")

        palabras = linea.lower().split()

        for palabra in palabras:

            # Comparar con la palabra anterior
            if palabra == palabra_anterior:
                print(
                    f"Palabra repetida encontrada en la línea "
                    f"{numero_linea}: '{palabra}'"
                )

            palabra_anterior = palabra
            linea_anterior = numero_linea

    archivo.close()

except FileNotFoundError:
    print("Error: El archivo no existe.")

except Exception as e:
    print("Error durante el procesamiento del archivo:")
    print(e)
