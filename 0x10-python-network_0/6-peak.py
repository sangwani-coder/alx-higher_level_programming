#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
    A peak is an Element in An array if its NOT smaller
    than its neighbours.
"""

def find_peak(list_of_integers):
    """ returns the a peak in a an unsored list"""

    arr = list_of_integers
    if arr == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return arr[0]
    elif size == 2:
        return max(arr)

    half = int(size / 2)
    peak = arr[half]
    if peak > arr[half - 1] and peak > arr[half + 1]:
        return peak    
    elif peak < arr[half - 1]:
        return find_peak(arr[:half])
    else:
        return find_peak(arr[half + 1:])
