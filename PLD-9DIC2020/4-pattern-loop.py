#!/usr/bin/python3
"""
4. Write a Python program to construct the following pattern,
using a nested for loop.
"""

for i in range(6):
        # print(i)
        for j in range(i):
                print("* ", end="")
        print()

for i in range(1, 5):
        # print(i)
        for j in range(5 - i):
                print("* ", end="")
        print()
