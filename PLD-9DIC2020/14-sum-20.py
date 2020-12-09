#!/usr/bin/python3
"""
14. Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20.
"""

print("******SUMAR DOS NUMEROS******")
n1 = int(input("Ingrsa el primer numero: "))
n2 = int(input("Ingrsa el segundo numero: "))

if n1 + n2 in range(15, 20):
        print("Resultado: {}".format(20))
else:
        print("Resultado: {}".format(n1 + n2))
