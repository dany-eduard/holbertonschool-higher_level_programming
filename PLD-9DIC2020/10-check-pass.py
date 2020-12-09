#!/usr/bin/python3
import re  # Module of regular expression is used with search() 

"""
10. Write a Python program to check the validity of password
input by users.

Validation:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

passwd = input('Type your password: ')

letterLw = False
letterUp = False
number = False
length = False
char = False

for c in passwd:
        if (ord(c) >= 97 or ord(c) <= 122):
                letterLw = True
        if (ord(c) >= 65 or ord(c) <= 90):
                letterLw = True
        if c.isdigit():
                """or (c >= 0 and c <= 9)"""
                number = True
        if len(passwd) > 6 and len(passwd) < 16:
                length = True
        if re.search("[!_$#@]", passwd):
                char = True

if letterLw == True and letterLw == True and number == True and length == True and char == True:
        print("Your password is sure!")
else:
        print("Your password is NOT sure!")


