#!/usr/bin/python3
"""
Function that prints a square of '#' characters
"""


def print_square(size):
    """Check if size is an integer else throw TypeError"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is None:
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
