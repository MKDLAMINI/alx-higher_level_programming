#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length_of_list = len(my_list)
    fresh_list = []
    for i in range(length_of_list):
        if my_list[i] % 2 == 0:
            fresh_list.append(True)
        else:
            fresh_list.append(False)
    return fresh_list
