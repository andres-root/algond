#!/usr/bin/python3


def partition(arr, l, r):
    p = arr[r]

    while r is not l:
        item = arr[l]

        if item <= p:
            l += 1
            continue

        # Place the item before the pivot at left index
        arr[l] = arr[r - 1]

        # Move the pivot one slot to the left
        arr[r - 1] = p

        # Place item at pivot's previous location
        arr[r] = item 

        # Update pivot index
        r -= 1
    return r

def quick_sort(arr, l, r):
    if r <= l:
        return False
    
    p = partition(arr, l, r)
    
    quick_sort(arr, l, (p - 1))
    quick_sort(arr, (p + 1), r)
    

if __name__ == '__main__':
    arr = [8, 3, 1, 7, 0, 10, 2]
    quick_sort(arr, 0, (len(arr) - 1))
    print(arr)