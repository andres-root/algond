#!/usr/bin/env python3

import random


def get_min_max(arr):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    n_min = 0
    n_max = 0

    for n in arr:
        if n < n_min:
            n_min = n
        if n > n_max:
            n_max = n
    
    return n_min, n_max


if __name__ == '__main__':
    ## Example Test Case of Ten Integers
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
