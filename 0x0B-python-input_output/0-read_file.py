#!/usr/bin/python3
"""Define a function that reads a utf-8 file"""


def read_file(filename=""):
    """Open the utf-8 file using the "with" keyword"""
    with open(filename, 'r', encoding="utf-8") as f:
        """Read the content of the file"""
        rf = f.read()
        print(rf, end="")
