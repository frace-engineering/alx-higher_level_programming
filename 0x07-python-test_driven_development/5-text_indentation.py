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
    for ch in text:
        if (ch == ' ' or ch == '\t'):
           continue 
        print(ch, end="")
        if (ch == '.' or ch == '?' or ch ==':'):
            print("\n")
    print()
