#!/usr/bin/python#
n = int(input("Fibonacci of: "))


def fib(n):
        if n < 2:
                return n
        return fib(n - 1) + fib(n - 2)


for i in range(n):
        print(fib(i), end=' ')
print()
