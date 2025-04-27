#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) == 2:
        date, temp = parts
        print(f"{date}\t{temp}")
