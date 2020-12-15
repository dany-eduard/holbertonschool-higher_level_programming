#!/usr/bin/env python3


def no_c(my_string):
    new_string = ''
    for i in my_string:
        if not i in ['c', 'C']:
            new_string += i
    return new_string
