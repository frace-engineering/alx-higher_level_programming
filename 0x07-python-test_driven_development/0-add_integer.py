#!/usr/bin/python3
"""
The function "add_integer" adds two integers
"""


def add_integer(a, b=98):
    """
    Check if arguments are of the required type, else raise TypeError
    """
    if a is None and b is None:
        raise TypeError("add_integer() missing 1 required"
                        "positional argument: 'a'")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise OverflowError("a too large")
    if b + 1 == b:
        raise OverflowError("b too large")
    """
    Convert arguments to int if they are float and return the sum
    """
    return int(a) + int(b)
