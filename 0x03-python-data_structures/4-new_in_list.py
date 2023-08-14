#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    new_list = my_list[:]
    list_len = len(my_list)
    digits = range(list_len)
    digits_list = list(digits)
    if idx not in digits_list:
        return new_list
    for i in digits_list:
        if i == idx:
            new_list[idx] = element
            return new_list

