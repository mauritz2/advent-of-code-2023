with open("day-13-data.txt") as f:
    all_terrains = []
    terrain = [] 
    data = f.readlines()
    data = [row.strip() for row in data]

    for row in data:
        # Requires adding two spaces to the data so all terrains are captured
        if len(row) == 0:
            all_terrains.append(terrain)
            terrain = []
        else:
            terrain.append(row)

def is_imperfect_mirror(above, below):
    smudge_matches = 0
    perfect_matches = 0
    for a, b in zip(above, below):
        if a == b:
            perfect_matches += 1
            continue
        non_matching_chars = 0
        for char1, char2 in zip(a, b):
            if char1 != char2:
                non_matching_chars += 1
            if non_matching_chars > 1:
                break
        else:
            if non_matching_chars == 1:
                smudge_matches += 1

    if smudge_matches == 1 and perfect_matches == len(above) - 1:
        return True
    else:
        return False

def find_horizontal_mirror_pos(terrain):
    row_len = len(terrain)
    for i in range(1, len(terrain)):
        rows_above = i
        rows_below = row_len - rows_above
        max_mirror_length = min(rows_below, rows_above)

        above = terrain[i - max_mirror_length:i]
        below = terrain[i:i + max_mirror_length]
        below.reverse()

        if is_imperfect_mirror(above, below):
            mirror_loc = i
            return mirror_loc
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


# Find the smudge
# Correct the smudge
# Find the new line