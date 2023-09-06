#!/usr/bin/python3
"""
The function "add_integer" adds two integers
"""


def add_integer(a, b=98):
    """
    args:
        a must be an integer or float
        b must be an integer or float
    raises:
        TypeError if not correct type
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise OverflowError("a too large")
    if b + 1 == b:
        raise OverflowError("b too large")
    """ Convert arg to int if they are float and return the sum """
    return int(a) + int(b)
