#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    idx_list = [i for i, el in enumerate(my_list) if el == search]
    for idx in idx_list:
        new_list[idx] = replace
    return new_list
