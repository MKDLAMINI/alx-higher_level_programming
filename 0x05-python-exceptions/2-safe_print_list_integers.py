#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tally = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            tally += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (tally)
