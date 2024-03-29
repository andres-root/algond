#!/usr/bin/env python3

import csv
import os
import re
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

def is_bangalore_phone(phone):
    return re.search('\(080\)', phone) is not None

def find_area_code(phone):
    return re.search('\(.*?\)', phone)

def clean_text(text):
    return text.strip().replace('(', '').replace(')', '')

def print_message(records, percentaje):
    print('The numbers called by people in Bangalore have codes:')

    for n in records:
        print(n)
    
    print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percentaje))

def bangalore_codes(records):
    """
    TASK 3:
    (080) is the area code for fixed line telephones in Bangalore.
    Fixed line numbers include parentheses, so Bangalore numbers
    have the form (080)xxxxxxx.)

    Part A: Find all of the area codes and mobile prefixes called by people
    in Bangalore.
    - Fixed lines start with an area code enclosed in brackets. The area
    codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always start with 7, 8 or 9.
    - Telemarketers' numbers have no parentheses or space, but they start
    with the area code 140.

    Print the answer as part of a message:
    "The numbers called by people in Bangalore have codes:"
    <list of codes>
    The list of codes should be print out one per line in lexicographic order with no duplicates.

    Part B: What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?

    Print the answer as a part of a message::
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits
    """
    bangalore = []

    bangalore_total = 0
    total = 0
    
    for record in records:
        if is_bangalore_phone(record[0]):
            total += 1
            
            phone = record[1]

            if is_bangalore_phone(phone):
                bangalore_total += 1

            if find_area_code(str(phone)) is None:
                code = phone[:4]
            else:
                code = clean_text(find_area_code(phone).group())
            
            bangalore.append(code)

    return sorted(list(set(bangalore))), round(bangalore_total / total, 2)


if __name__ == '__main__':
    records = read_files()

    bangalore_phones_list, percentaje = bangalore_codes(records)
    print_message(bangalore_phones_list, percentaje)
