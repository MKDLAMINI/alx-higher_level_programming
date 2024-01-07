#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tp = my_list[:]
    if idx < 0:
        return tp
    if idx > len(my_list) - 1:
        return tp
    tp[idx] = element
    return tp
