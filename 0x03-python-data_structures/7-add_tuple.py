#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    num1 = tuple_a[0] + tuple_b[0]
    num2 = tuple_a[1] + tuple_b[1]
    print(tuple_a)
    return num1, num2
