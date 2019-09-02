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

    with open((dir_path / 'calls.csv'), 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

    return calls

def format_message(call):
    return '{0} spent the longest time, {1} seconds, on the phone during September 2016.".'.format(call['number'], call['duration'])

def max_time_spent(records):
    """
    TASK 2: Which telephone number spent the longest time on the phone
    during the period? Don't forget that time spent answering a call is
    also time spent on the phone.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during 
    September 2016.".
    """
    longest_call = {
        'number': -1,
        'duration': 0,
    }

    for call in records:
        if int(call[3]) > longest_call['duration']:
            longest_call['number'] = call[1]
            longest_call['duration'] = int(call[3])
        
    return longest_call


if __name__ == '__main__':
    records = read_files()

    max_call = max_time_spent(records)

    print(format_message(max_call))
