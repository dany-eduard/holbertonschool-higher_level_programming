#!/usr/bin/python3

"""
2. Write a Python program to convert temperatures to and from celsius, fahrenheit. 
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

i = int(input("*****MENU*****\n1. C° a F°\n2. F° a C°\nIngrese una opción: "))

if i == 1:
        c = int(input("Ingresa una temperatura en C°: "))
        f = (c * 9/5) + 32
        print("{}°C is {:0.0f} in Fahrenheit".format(c, f))
elif i == 2:
        f = int(input("Ingresa una temperatura en F°: "))
        c = (f - 32) * 5/9
        print("{}°F is {:0.0f} in Celsius".format(f, c))
