#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elems = 0
    if isinstance(x, int):
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{}".format(my_list[i]), end="")
                    num_of_elems += 1
            except IndexError:
                continue
        print("")
    return (num_of_elems)
