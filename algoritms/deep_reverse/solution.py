#!/usr/bin/env python3

def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)

def deep_reverse_udacity(arr):
    """
    Function to deep_reverse an input list
    """
    return deep_reverse_func(arr, 0)

def deep_reverse_func(arr, index):
    """
    Recursive function to deep_reverse the input list
    """
    # Base Case
    if index == len(arr):
        return list()
    
    output = deep_reverse_func(arr, index + 1)
    
    # if element is a list --> deep_reverse the list
    if is_list(arr[index]):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]
        
    output.append(to_append)
    return output


# My solutions
def deep_reverse(arr):
    return reverse(arr)

def reverse(arr):
    if len(arr) == 1:
        if isinstance(arr[0], list):
            sublist_item = arr[0]
            rev_sublist = reverse(sublist_item)

            return [rev_sublist]
        else:
            return [arr[0]]  
    
    rev = reverse(arr[1:])
    
    if isinstance(arr[0], list):
        sublist = arr[0]
        rev_copy = reverse(sublist)
        rev.append(rev_copy)
    else:
        rev.append(arr[0])
    
    return rev

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    print(output)
    
    if output == solution:
        return 'Pass'
    else:
        return 'Fail'


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    solution = [5, 4, 3, 2, 1]
    test_case = [arr, solution]
    result = test_function(test_case)
    print(result)

    arr = [1, 2, [3, 4, 5], 4, 5]
    solution = [5, 4, [5, 4, 3], 2, 1]
    test_case = [arr, solution]
    result = test_function(test_case)
    print(result)

    arr = [1, [2, 3, [4, [5, 6]]]]
    solution = [[[[6, 5], 4], 3, 2], 1]
    test_case = [arr, solution]
    result = test_function(test_case)
    print(result)

    arr =  [1, [2,3], 4, [5,6]]
    solution = [ [6,5], 4, [3, 2], 1]
    test_case = [arr, solution]
    result = test_function(test_case)
    print(result)
    