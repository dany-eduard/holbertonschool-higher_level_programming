#!/usr/bin/python3
"""
16. Write a Python program to calculate the sum and average
of n integer numbers (input from the user). Input 0 to finish.
"""
sum = 0
aver = 0
count = 1

while True:
        n = int(input("Write a number: "))
        if n == 0:
                break
        sum = sum + n
        aver = sum / count
        count += 1

print("-------------\nSum result: {}\nAverage reault: {:0.1f}".format(sum, aver))
