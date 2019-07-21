#!/usr/bin/env python3


class HashMap:
    def __init__(self, initial_size=10):
        self.bucket = [None for _ in range(initial_size)]
        self.prime = 37
        self.num_entries = 0
    
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    def get_bucket_index(self, key):
        return self.get_hash_code(key)
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket)
        current_coefficient = 1
        hash_code = 0

        for c in key:
            hash_code += ord(c) * current_coefficient
            current_coefficient = self.prime

        return hash_code

# Testing
hash_map = HashMap()

bucket_index = hash_map.get_bucket_index('abcd')
print(bucket_index)

hash_map = HashMap()

bucket_index = hash_map.get_bucket_index('bcda')
print(bucket_index)
