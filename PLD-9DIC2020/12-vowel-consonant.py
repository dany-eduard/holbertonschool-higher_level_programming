#!/usr/bin/python3
"""
12. Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.
"""

c = input("Input a letter of the alphabet: ")
if c in ('aeiouAEIOU'):
        print("{:s} is vowel.".format(c))
else:
        print("{:s} is consonant.".format(c))
