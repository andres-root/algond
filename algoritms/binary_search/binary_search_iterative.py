#!/usr/bin/env python3


def binary_search_iterative(array, target):
    '''Binary search algorithm using iteration
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    low = 0
    high = 0

    while low <= high:
        mid = (low + high)//2

        if array[mid] == target:
            return mid

        if target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1
