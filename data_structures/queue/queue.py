#!/usr/bin/env python3


class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.nex_index = 0
        self.front_index = -1
        self.queue_size = 0


if __name__ == '__main__':
    q = Queue()
    print(q.arr)
    print("Pass" if q.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")
