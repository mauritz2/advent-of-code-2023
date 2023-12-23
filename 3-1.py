import re
import string
from dataclasses import dataclass

num_pattern = re.compile(r"[0-9]+")
possible_machine_parts = []
symbols = [s for s in string.punctuation if s != '.']
total_score = 0

with open("day-3-data.txt") as f:
    data_raw = f.readlines()
    data = [f.strip() for f in data_raw]
    # Pad data to avoid index out of range errors
    total_rows = len(data)
    total_cols = len(data[0])
    row_padding = "." * total_rows
    data.insert(0, row_padding)
    data.append(row_padding)
    for i in range(total_rows + 1):
        data[i] = "." + data[i] + "."

def has_adjacent_symbol(match:re.match, current_row:int) -> bool:
    match_start = match.start()
    match_end = match.end()

    left_chars = data[current_row][match_start - 1]
    right_chars = data[current_row][match_end]
    upper_chars = data[current_row - 1][match_start - 1 : match_end + 1] 
    lower_chars = data[current_row + 1][match_start - 1 : match_end + 1] 
    all_chars = left_chars + right_chars + upper_chars + lower_chars
    unique_chars = set(all_chars)

    for char in unique_chars:
        if char in symbols:
            return True

    return False

# Loop through all machine parts and verify if valid part
for row_num, row in enumerate(data):
    matches = re.finditer(num_pattern, row)
    for match in matches:
        number = match.group(0)
        valid_part = has_adjacent_symbol(match, row_num)

        if valid_part:
            print(str(row_num) + " : " + str(number))
            total_score += int(number)
print(total_score)