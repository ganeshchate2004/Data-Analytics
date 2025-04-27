#!/usr/bin/env python3
import sys

current_date = None
temp_sum = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    date, temp = line.split('\t')

    temp = float(temp)

    if current_date == date:
        temp_sum += temp
        count += 1
    else:
        if current_date:
            # Output the average for previous date
            avg_temp = temp_sum / count
            print(f"{current_date}\t{avg_temp:.2f}")
        current_date = date
        temp_sum = temp
        count = 1

# Output the last date's average
if current_date:
    avg_temp = temp_sum / count
    print(f"{current_date}\t{avg_temp:.2f}")
