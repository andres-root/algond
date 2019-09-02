#!/usr/bin/env python3

import csv
import os
from pathlib import Path


def read_files():
    """
    Read file into texts and calls.
    It's ok if you don't understand how to read files.
    """
    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

    with open((dir_path / 'texts.csv'), 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open((dir_path / 'calls.csv'), 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

    return texts + calls

def format_message(x):
    return 'There are {} different telephone numbers in the records.'.format(x)

def clean_text(text):
    return text.strip().replace(' ', '')

def count_unique_records(records):    
    """
    TASK 1:
    How many different telephone numbers are there in the records? 
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    numbers = set()

    for record in records:
        numbers.add(record[0])
        numbers.add(record[1])

    return len(numbers)


if __name__ == '__main__':
    records = read_files()

    unique_records_count = count_unique_records(records)
    print(format_message(unique_records_count)
