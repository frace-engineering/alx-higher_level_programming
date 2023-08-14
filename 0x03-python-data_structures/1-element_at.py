#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list is None:
        return None
    list_len = len(my_list)
    digits = range(list_len)
    digits_list = list(digits)
    if idx not in digits_list:
        return None
    for i in digits_list:
        if i == idx:
            return my_list[idx]
