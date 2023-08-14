#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        return None
    digits = len(my_list)
    for digit in range(digits):
        print("{:d}".format(my_list[digit]))
