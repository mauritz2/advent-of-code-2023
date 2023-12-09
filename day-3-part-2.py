import math
import re

board = list(open('day-3-data.txt'))

symbol_locs = {}
for row in range(140):
    for column in range(140):
        if board[row][column] not in "0123456789.":
            symbol_locs[row, column] = []

for row_num, row_data in enumerate(board):
    for match in re.finditer(r'\d+', row_data):
        adjacent_locs = []
        for row in (row_num - 1, row_num, row_num + 1):
            for column in range(match.start() - 1, match.end() + 1):
                adjacent_locs.append((row,column))
        adjacent_locs = set(adjacent_locs)

        for overlap in adjacent_locs & symbol_locs.keys():
            symbol_locs[overlap].append(int(match.group()))

# Part 1
print(sum(sum(p) for p in symbol_locs.values()))

# Part 2
print(sum(math.prod(p) for p in symbol_locs.values() if len(p)==2))

# https://topaz.github.io/paste/#XQAAAQAcAgAAAAAAAAA0m0pnuFI8c+fPp4G3Y5M2miSs3R6AnrKm3fbDkugpdVsCgQOTZL/yzxGwy/N08UeBslxE7G36XluuSq4Y/2FE0+4nPcdj9lpkrrjBk5HRCFLEKuPjUV8tYPx04VDoJ1c6yyLzScmAGwNvzpPoqb5PkRyyy4dSEcuEDe/k0/U7h7pZVh4eTrNAIPsTNZohcltxuwuA4lrZSN37i0QZiufFpvLVyhV/dLBnmSr+2jwFcFE+W6OEIFQxK6MIJ2z7TWKj8lg6yV4yhJzTm+c+QHh2omzhGVLd2WdcHdhjmCyC+Btbr3yCqemYb/6tMUvz8VchnyHstx7QKKeLVmTOEyYqHH/qRDhlKXSQ23RWuPibCf4quQUPGpPDRsH4KITzLbIUVUdssnSp6ffcHO+dAISdzBOiznl5/+PI+jE=