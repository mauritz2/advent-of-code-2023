from functools import reduce

seeds, *mappings = open('day-5-data.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

def reverse_lookup(start, mapping) -> int:
    for row in mapping.split('\n')[1:]:
        destination, source, length = map(int, row.split())
        delta = start - destination
        if delta in range(length):
            return source + delta
    else:
        return start

def is_valid_seed(soil_id) -> bool:
    for i in range(0, len(seeds), 2):
        seed_range = range(seeds[i], seeds[i] + seeds[i + 1])
        if soil_id in seed_range:
            return True
    return False
                           
mappings.reverse()

loc = 0
while True: 
    # Takes a few hours to run
    potential_seed = reduce(reverse_lookup, mappings, int(loc))
    if is_valid_seed(potential_seed):
        break
    loc += 1

print(f"Lowest location that corresponds to a seed is {loc}")

