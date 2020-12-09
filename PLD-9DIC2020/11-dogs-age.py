#!/usr/bin/python3
"""
11. Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
"""

age = int(input("Enter the age of the dog in human years: "))
print("Input a dog's age in human years: {}".format(age))

if age < 0:
        print("Age not valid, enter a positive number")
else:
        if age <= 2:
                age_d = age * 10.5
        elif age > 2:
                age_d = 21 + (age - 2) * 4
        print("The dog's age in dog's years is: {}".format(age_d))
