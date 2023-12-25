from itertools import pairwise

with open("inputs/18.txt") as f:
    output = [row.split() for row in f.readlines()]
    directions, steps, hexes = zip(*output)
    steps = [int(step) for step in steps]

edge_locs = [(500,250)]

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


all_x = [loc[0] for loc in edge_locs]
x_max, x_min = max(all_x), min(all_x)

total_difference = 0

for i in range(x_min, x_max + 1):
    all_borders_in_row = sorted([loc[1] for loc in edge_locs if loc[0] == i])
    if len(all_borders_in_row) % 2 == 0
    for j in range(0, len(all_borders_in_row), 2):  
        border_start = all_borders_in_row[j]
        border_end = all_borders_in_row[j + 2]
        difference = border_end - border_start
        total_difference += difference




# my_grid = [["."] * 800 for _ in range(800)]

# for el in edge_locs:
#     my_grid[el[0]][el[1]] = "#"

# total_filled = 0
# total_filled += len(set(edge_locs))

# for i, row in enumerate(my_grid):
#     row_str = "".join(row)
#     fill_end = 0
#     next_fill_start = row_str.find("#.")
#     while next_fill_start != -1:
#         fill_end = row_str.find(".#", next_fill_start)
#         if fill_end != -1:
#             assert fill_end > next_fill_start
#             row_fill = (fill_end - next_fill_start)
#             total_filled += row_fill
#             print(f"The row is {i}")
#             print("".join(row))
#             print(f"The score is {row_fill}")
#             print("-----------------------")
#             next_fill_start = row_str.find("#.", fill_end + 2)
#         else:
#             break

# print("Printing total filled!")
# print(total_filled)        

# Right answer: 49897
# My answer +2 : 47295
# My answer: 48975