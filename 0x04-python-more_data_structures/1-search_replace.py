#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    new_list = my_list.copy()
    idx = range(len(new_list))
    for x in new_list:
        for i in idx:
            if new_list[i] == search:
                new_list[i] = replace
    return new_list
