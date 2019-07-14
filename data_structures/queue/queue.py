#!/usr/bin/env python3


class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.nex_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        self.arr[self.nex_index] = value
        self.queue_size += 1
        self.nex_index += (self.nex_index + 1) % len(self.arr)

        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        return self.queue_size
    
    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        return arr[self.front_index]


if __name__ == '__main__':
    q = Queue()
    print(q.arr)
    print("Pass" if q.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")
