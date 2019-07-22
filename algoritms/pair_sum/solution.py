#!/usr/bin/env python3


def pair_sum_sorted(arr, t):
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

def pair_sum(arr, t):
    mem = {}
    l = 0
    h = len(arr)
    mem[arr[l]] = l

    for i in range(1, h):
        d = t - arr[i]

        if d in mem.keys():
            return (mem[d], i)

        mem[arr[i]] = i
    
    return False


if __name__ == '__main__':
    arr = [3, 4, 6, 7, 12, 14, 2, 1, 0, 9]
    t = 26
    pair = pair_sum(arr, t)
    print(pair)
