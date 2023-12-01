#!/usr/bin/python3
# finds a peak in a list of unsorted integers.


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = size // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        high = find_peak(list_of_integers[mid:])
        return high > peak ? high : peak 
        low = find_peak(list_of_integers[:mid])
        return low > peak ? high : peak 

    

