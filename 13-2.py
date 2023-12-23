with open("day-13-data.txt") as f:
    all_terrains = []
    terrain = []
    for row in f:
        row = row.strip()
        if row:
            terrain.append(row)
        else:
            all_terrains.append(terrain)
            terrain = []
    if terrain:
        all_terrains.append(terrain)

def is_imperfect_mirror(above, below):
    perfect_matches = 0
    smudge_matches = 0

    for a, b in zip(above, below):
        if a == b:
            perfect_matches += 1
        elif sum(char1 != char2 for char1, char2 in zip(a, b)) == 1:
            smudge_matches += 1

    return smudge_matches == 1 and perfect_matches == len(above) - 1

def find_horizontal_mirror_pos(terrain):
    row_len = len(terrain)
    for i in range(1, len(terrain)):
        rows_above = i
        rows_below = row_len - rows_above
        max_mirror_length = min(rows_below, rows_above)
        above = terrain[i - max_mirror_length:i]
        below = terrain[i:i + max_mirror_length][::-1]
        if is_imperfect_mirror(above, below):
            return i
    return None

total_sum = 0
for terrain in all_terrains:
    mirror_loc = find_horizontal_mirror_pos(terrain)
    if mirror_loc is not None:
        total_sum += (100 * mirror_loc)
    else:
        terrain_t = ["".join(row) for row in (zip(*terrain))]
        mirror_loc = find_horizontal_mirror_pos(terrain_t)
        total_sum += mirror_loc
print(total_sum)
