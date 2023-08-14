#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list is None:
        return None
    list_len = len(my_list)
    digits = range(list_len)
    digits_list = list(digits)
    if idx not in digits_list:
        return my_list
    for i in digits_list:
        if i == idx:
            my_list[idx] = element
            return my_list

