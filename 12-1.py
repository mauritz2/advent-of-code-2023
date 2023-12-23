

with open("day-12-data.txt") as f:
    records, num_arrangements = zip(*[row.strip().split() for row in f])
    
    num_arrangements = [list(map(int, row.split(","))) for row in num_arrangements]

OPTIONS = ["#", "."]

def calc_possible_arrangements(record:str, answer:list[int]):
    print(re)
    def count_segments(s):
        return [len(seg) for seg in s.split('.') if seg]

    if '?' not in record:
        segment_counts = count_segments(record)
        if segment_counts == answer:
            return 1
        else:
            return 0

    next_unknown_pos = record.find('?')
    total_arrangements = 0

    for replacement in ['.', '#']:
        new_record = record[:next_unknown_pos] + replacement + record[next_unknown_pos + 1:]
        total_arrangements += calc_possible_arrangements(new_record, answer)

    return total_arrangements

total_arrangements = 0
for record, num_arrangmenent in zip(records, num_arrangements):
    total_arrangements += calc_possible_arrangements(record, num_arrangmenent)

print(total_arrangements)