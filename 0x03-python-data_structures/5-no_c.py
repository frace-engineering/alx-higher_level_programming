#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new = ""
    for char in my_string:
        if char.lower() != 'c':
            new += char
    return new
