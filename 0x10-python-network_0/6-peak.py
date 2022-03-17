#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
    A peak is an Element in An array if its NOT smaller
    than its neighbours.
"""

def find_peak(list_of_integers):
    """Iterates list_of_integers to find a "peak"
        returns the peak numbers.
    """
    arr = list_of_integers
    size = len(list_of_integers)

    if size == 1:
        return arr[0]
    if size == 0:
        return
    else:
        for p in range(size):
            if arr[p] >= arr[p-1] and arr[p] >= arr[p+1]:
                return arr[p]
