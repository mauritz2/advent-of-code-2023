from functools import reduce

seeds, *mappings = open('day-5-data.txt').read().split('\n\n')
seeds = map(int, seeds.split()[1:])

def lookup(start, mapping):
    for row in mapping.split('\n')[1:]:
        destination, source, length = map(int, row.split())
        delta = start - source
        if delta in range(length):
            return destination + delta
    else:
        return start

locations = []
for s in seeds:
    location = reduce(lookup, mappings, int(s))
    locations.append(location)
print(min(locations))

