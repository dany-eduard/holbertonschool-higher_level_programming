#!/usr/bin/python3
"""
3. Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses
wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message,
and the program will exit.
"""

import random

x = True
while x == True:
        num = int(input("Adivina el numero: "))
        i = random.randint(1,10)
        print("Random number: ", i)
        if num == i:
                print("Well guessed!")
                x = False
