#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    strlen = len(my_string)
    str_idx = range(strlen - 2)
    for i in str_idx:
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = my_string[:i] + my_string[i + 1:]
    return my_string
