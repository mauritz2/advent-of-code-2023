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

def find_horizontal_mirror_pos(terrain):
    row_len = len(terrain)
    for i in range(1, len(terrain)):
        rows_above = i
        rows_below = row_len - rows_above
        max_mirror_length = min(rows_below, rows_above)

        above = terrain[i - max_mirror_length:i]
        below = terrain[i:i + max_mirror_length]

        if sorted(above) == sorted(below):
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
