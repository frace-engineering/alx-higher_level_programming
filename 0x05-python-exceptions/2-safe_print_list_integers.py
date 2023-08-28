#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_of_elems = 0
    if isinstance(x, int):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                num_of_elems += 1
            except (TypeError, ValueError):
                continue
        print("")
    return (num_of_elems)
