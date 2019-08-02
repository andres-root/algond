#!/usr/bin/env python3

from collections import deque


def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    l = 0
    i = 0
    j = 0
    n = len(arr) - 1

    mid = (l + n) // 2

    while j <= n:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid:
            arr[j], arr[n] = arr[j], arr[n]
            n -= 1
        else:
            j += 1
    return arr

def hash_table_sort_012(arr):
    flag = {
        0: [],
        1: [],
        2: [],
    }

    for n in arr:
        flag[n].append(n)
    
    return flag[0] + flag[1] + flag[2]

def queue_sort_012(arr):
    q = [1] * len(arr)
    l = 0
    h = len(arr) - 1
    m = 0
    for n in arr:
        if n == 0:
            m = q[l]
            q[l] = n
            q[l + 1] = m
            l += 1
        elif n == 2:
            m = q[h]
            q[h] = n
            q[h - 1] = m
            h -= 1
        # else:
        #     q[l + 1] = q[l]
        #     q[l] = n
        # print(q)

    return q

def test_function(test_case):
    sorted_array = queue_sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
