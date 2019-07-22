#!/usr/bin/env python3


def pair_sum(arr, t):
    l = 0
    r = len(arr) - 1

    while l <= r:
        s = arr[l] + arr[r]
        
        if s == t:
            return (arr[l], arr[r])
        elif s < t:
            l += 1
        else:
            r -= 1

    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    t = 9
    pair = pair_sum(arr, t)
    print(pair)
