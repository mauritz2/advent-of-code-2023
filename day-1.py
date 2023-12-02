
import re

with open("day-1-data.txt") as f:
    data_raw = f.readlines()
    data = [line.strip() for line in data_raw]

digits_re = re.compile("[0-9]")
total_sum_str = []

for row in data:
    match = re.findall(digits_re, row)
    total_sum_str.append(match[0] + match[-1])

total_sum = sum(int(i) for i in total_sum_str)
print(total_sum)