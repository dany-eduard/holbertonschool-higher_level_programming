#!/usr/bin/python3
for i in range(0, 100):
    firtDigit = i / 10
    lastDigit = i % 10
    if firtDigit < lastDigit and i != 89:
        print('{:02}, '.format(i), end='')
    elif i == 89:
        print('{}'.format(i))
