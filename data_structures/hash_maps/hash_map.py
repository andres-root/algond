#!/usr/bin/env python3


class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.prime = 37
        self.num_entries = 0
    
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    def get_bucket_index(self, key):
        print(self.get_hash_code(key), 'Index')
        return self.get_hash_code(key)
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0

        for c in key:
            hash_code += ord(c) * current_coefficient
            hash_code = hash_code % num_buckets  # Compress hash_code
            current_coefficient = self.prime
            current_coefficient = current_coefficient % num_buckets  # Compress coefficient

        return hash_code % num_buckets  # One last compression before returning


if __name__ == '__main__':
    # Testing
    hash_map = HashMap()

    bucket_index = hash_map.get_bucket_index('abcd')
    print(bucket_index)

    hash_map = HashMap()

    bucket_index = hash_map.get_bucket_index('bcda')
    print(bucket_index)
