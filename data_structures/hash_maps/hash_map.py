#!/usr/bin/env python3


class HashTable:
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash_value = self.calculate_hash_value(string)

        if hash_value is not -1:
            if self.table[hash_value] is not None:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]
    
    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        
        if hash_value is not -1:
            if self.table[hash_value] is not None:
                if string in self.table[hash_value]:
                    return hash_value
        
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value
