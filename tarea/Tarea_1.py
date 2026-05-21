#Ejercicio 1
#Modifica el programa que resuelve la ecuación cuadratica (vista en la ayudantía), de tal forma que tenga solución cuando el discriminante sea menor a cero.

import cmath

a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
c = float(input("Ingresa c: "))

d = b**2 - 4*a*c

x1 = (-b + cmath.sqrt(d)) / (2*a)
x2 = (-b - cmath.sqrt(d)) / (2*a)

print("Las soluciones son:")
print(x1)
print(x2)

#Ejercicio 2
#Desarrollar un programa que calcule la suma de los dígitos de cualquier número entero positivo introducido por el usuario.

numero = int(input("Ingresa un número entero positivo: "))

suma = 0

while numero > 0:
    suma += numero % 10
    numero //= 10

print("La suma de los dígitos es:", suma)

#Ejercicio 3
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Ingresa una palabra: ")

if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
#Ejercicio 4
#Elabora un programa que genere una sucesión de números aleatorios en el intervalo [0.01,0.20], cuya suma sea menor que 1.50
import random

suma = 0

while suma < 1.50:
    num = random.uniform(0.01, 0.20)
    suma += num
    print(num)

print("Suma total:", suma)
#Ejercicio 5
#i. Construye un programa que diga si un número entero es o no primo

n = int(input("Ingresa un número: "))

es_primo = True

if n <= 1:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es primo")
else:
    print("No es primo")

#ii. Elabora un programa que muestre los primeros N números primos. (N es solicitao por el usuario).

N = int(input("¿Cuántos primos quieres?: "))

contador = 0
numero = 2

while contador < N:
    es_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(numero)
        contador += 1

    numero += 1
#Ejercicio 6
#Haz un programa que te regrese los primeros 100 términos de la sucesión de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, · · ·)
a = 1
b = 1

print(a)
print(b)

for i in range(98):
    c = a + b
    print(c)
    a = b
    b = c
