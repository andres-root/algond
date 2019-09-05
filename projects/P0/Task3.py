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

def clean_text(text):
    return text.strip().replace(' ', '').replace('(080)', '')

def print_message(records):
    print('The numbers called by people in Bangalore have codes:')

    for n in records:
        print(n)

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
    bangalore_phones = []
    
    for record in records:
        if is_bangalore_phone(record[0]):
            phone = int(clean_text(record[0]))
            
            if phone not in bangalore_phones:
                bangalore_phones.append(phone)
        
    return sorted(bangalore_phones)


if __name__ == '__main__':
    records = read_files()

    bangalore_phones_list = bangalore_codes(records)
    print_message(bangalore_phones_list)

