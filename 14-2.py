# By u/Domy__

CYCLES = 1000000000

with open("day-14-data.txt", "r") as file:
    input = tuple(file.read().splitlines())


def slide_rocks_north(grid):
    # transpose
    grid = list(map("".join, zip(*grid)))
    new_grid = []

    for row in grid:
        ordered_rows = []
        for group in row.split("#"):
            ordered_rows.append("".join(sorted(group, reverse=True)))

        new_grid.append("#".join(ordered_rows))

    return tuple(list(map("".join, zip(*new_grid))))


def print_grid(grid):
    for row in grid:
        print(row)
    print()


# 1 cycle = move rocks north, west, south, east
def cycle(grid):
    for _ in range(4):
        grid = slide_rocks_north(grid)
        # rotare 90 degrees
        grid = tuple(["".join(row[::-1]) for row in zip(*grid)])

    return grid


solution1 = 0
solution2 = 0

grid_slided = slide_rocks_north(input)
solution1 = sum(
    row.count("O") * (len(grid_slided) - i) for i, row in enumerate(grid_slided)
)

print("Solution 1:", solution1)

seen = {input}
seen_list = [input]

grid_cycle = input
for i in range(CYCLES):
    grid_cycle = cycle(grid_cycle)
    # print_grid(grid_cycle)

    if grid_cycle in seen:
        break
    seen.add(grid_cycle)
    seen_list.append(grid_cycle)

first_cycle_grid_index = seen_list.index(grid_cycle)
final_grid = seen_list[
    (CYCLES - first_cycle_grid_index) % (i + 1 - first_cycle_grid_index)
    + first_cycle_grid_index
]

solution2 = sum(
    row.count("O") * (len(final_grid) - i) for i, row in enumerate(final_grid)
)
print("Solution 2:", solution2)