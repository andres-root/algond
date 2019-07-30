#!/usr/bin/env python3


def rotated_binary_search(array, target):
    '''Binary search algorithm using iteration
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    low = 0
    last = len(array) - 1
    high = last

    while low <= high:
        mid = (low + high)//2

        if array[mid] == target:
            return mid

        if target > array[high]:
            high = mid - 1
        elif target < array[low]:
            low = mid + 1
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_binary_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
