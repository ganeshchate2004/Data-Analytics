#!/usr/bin/env python3

import sys

current_numbers = []

# Read mapper output from stdin
for line in sys.stdin:
    number, _ = line.strip().split('\t')
    current_numbers.append(int(number))

# Sort the collected numbers
current_numbers.sort()

# Output the sorted numbers
for number in current_numbers:
    print(number)
