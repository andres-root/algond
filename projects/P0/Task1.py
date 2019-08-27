#!/usr/bin/env python3

import csv
import os


def read_files():
    """
    Read file into texts and calls.
    It's ok if you don't understand how to read files.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)


def format_message(x):
    return 'There are {} different telephone numbers in the records.'.format(x)

def count_unique_records(records):    
    """
    TASK 1:
    How many different telephone numbers are there in the records? 
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    numbers = set()
    for call in range(len(records)):
        numbers.add(call[0])
        numbers.add(call[1])

    records_set = set(records)
    return records_set.size


if __name__ == '__main__':
    unique_records_count = count_unique_records(calls)

    print(unique_records_count)
