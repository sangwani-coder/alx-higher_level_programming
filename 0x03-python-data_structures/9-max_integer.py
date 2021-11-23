#!/usr/bin/python3
def max_integer(my_list=[]):
    Max = my_list[0]
    if len(my_list) < 1:
        return None
    else:
        for i in my_list:
            if i > Max:
                Max = i
    return (Max)
