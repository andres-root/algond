#!/usr/bin/env python3


def binary_search_recursive(array, target, low=0, high=(len(array) - 1)):
    '''Binary search algorithm using recursion
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    while low <= high:
        mid = (low + high)//2

        if array[mid] == target:
            return mid

        if target < array[mid]:
            return binary_search_recursive(array, target, low, (mid - 1))
        else:
            return binary_search_recursive(array, target, (mid + 1), high)
    
    return -1
