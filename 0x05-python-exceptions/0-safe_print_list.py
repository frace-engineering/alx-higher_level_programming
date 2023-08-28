#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elems = 0
    if isinstance(x, int) and x > 0:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    num_of_elems += 1
            except IndexError:
                break
        print("")
    return (num_of_elems)
