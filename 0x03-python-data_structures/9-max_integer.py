#!/usr/bin/python3
def max_integer(my_list=[]):
    Max = 0
    tmp = 0
    for i in my_list:
        tmp = i
        if tmp > Max:
            Max = tmp
    return (Max)
