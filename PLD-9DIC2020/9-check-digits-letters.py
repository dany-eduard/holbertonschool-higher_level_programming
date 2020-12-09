#!/usr/bin/python3
"""
9. Write a Python program that accepts a string and calculate
the number of digits and letters.
Sample Data: Python 3.2
Expected Output:

Letters 6
Digits 2
"""

word = input("Write a word: ")
l = 0; d = 0

for c in word:
        if c.isalpha():
                l += 1
        elif c.isdigit():
                d += 1

print('Letters {}\nDigitd {}'.format(l, d))
