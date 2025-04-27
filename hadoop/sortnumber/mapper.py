#!/usr/bin/env python3

import sys

# Read each line from stdin
for line in sys.stdin:
    # Remove whitespace and split into numbers if multiple numbers per line
    numbers = line.strip().split()
    for number in numbers:
        # Emit each number with a dummy value
        print(f"{number}\t1")
