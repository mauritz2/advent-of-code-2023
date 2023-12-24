with open("inputs/18.txt") as f:
    output = [row.split() for row in f.readlines()]
    directions, steps, hexes = zip(*output)
    steps = [int(step) for step in steps]

edge_locs = [(500,500)]

movement = {
    "U":(-1, 0),
    "D":(1, 0),
    "R":(0, 1),
    "L":(0, -1),
}

for direction, num_steps in zip(directions, steps):
    m = movement[direction]
    for _ in range(num_steps):
        new_pos = (edge_locs[-1][0] + m[0], edge_locs[-1][1] + m[1])
        if new_pos[0] < 0 or new_pos[1] < 0:
            raise ValueError()
        edge_locs.append(new_pos)

my_grid = [["."] * 10000 for _ in range(10000)]
#for el in edge_locs:
#    my_grid[el[0]][el[1]] = "#"

total_filled = 0
total_filled += len(set(edge_locs))

for row in my_grid:
    row_str = "".join(row)
    fill_start = row_str.find("#.")
    if fill_start != -1:
        fill_end = row_str.find(".#", fill_start)
        if fill_end != -1:
            total_filled += (fill_end - fill_start)

print("Printing total filled!")
print(total_filled)        
