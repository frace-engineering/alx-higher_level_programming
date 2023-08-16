#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    total = 0
    for n in set(my_list):
        total += n
    return total
