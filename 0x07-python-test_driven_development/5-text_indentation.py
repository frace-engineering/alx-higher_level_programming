#!/usr/bin/python3
"""
Function that prints a text and 2 new lines after each of ".,?:"
"""


def text_indentation(text):
    """Check if text is an empty string"""
    if text is None:
        return None
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for ch in text:
        if (ch == '.' or ch == '?' or ch == ':'):
            print(ch, end="")
            print("\n")
            flag = 1
        else:
            if (flag == 0):
                print(ch, end="")
            else:
                if (ch == ' ' or ch == '\t'):
                    pass
                else:
                    print(ch, end="")
                    flag = 0
