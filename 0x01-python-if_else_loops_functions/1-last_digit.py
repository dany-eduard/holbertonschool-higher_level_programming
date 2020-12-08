#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10  # Use abs to get the absolute value

if number <= 0:
        lastdigit *= -1

if lastdigit > 5:
        show = 'greater than 5'
elif lastdigit == 0:
        show = '0'
elif lastdigit < 6:
        show = 'less than 6 and not 0'

print('Last digit of {:d} is {:d} and is {:s}'.format(number, lastdigit, show))
