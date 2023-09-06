#!/usr/bin/python3
"""
Function that prints a text and 2 new lines after each of ".,?:"
"""


def text_indentation(text):
    """Check if text is an empty string"""
    check = ['.', '?', ':']
    if text is None:
        return None
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for index, character in enumerate(text):
        if character in check:
            if character != text[0] or character != text[-1]:
                print("{:s}".format(character), end="")
                print("\n")
        print("{:s}".format(character), end="")
