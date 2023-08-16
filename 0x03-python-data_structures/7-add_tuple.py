#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        tuple_a = (0, 0)
    elif (len(tuple_a) == 1):
        tuple_a = (tuple_a[0], 0)
    else:
        tuple_a = (tuple_a[0], tuple_a[1])
    if (len(tuple_b) == 0):
        tuple_b = (0, 0)
    elif (len(tuple_b) == 1):
        tuple_b = (tuple_b[0], 0)
    else:
        tuple_b = (tuple_b[0], tuple_b[1])
    a1, a2 = tuple_a
    b1, b2 = tuple_b
    s1 = a1 + b1
    s2 = a2 + b2
    tuple_s = (s1, s2)
    return tuple_s
