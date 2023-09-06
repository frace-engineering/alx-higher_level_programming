#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise OverflowError("a too large")
    if b + 1 == b:
        raise OverflowError("b too large")
    return int(a) + int(b)
