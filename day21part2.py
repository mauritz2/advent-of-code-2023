from functools import cache

with open("inputs/day21.txt") as f:
    grid = f.readlines()
    grid = [row.strip() for row in grid]
    start_pos = None
    for i, row in enumerate(grid):
        s_pos = row.find("S")
        if s_pos != -1:
            start_pos = (i, s_pos)
            break
    grid = [[c for c in row] for row in grid]
    grid[start_pos[0]][start_pos[1]] = "."

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Check fewer locations
    # Figure out which ones we don't have to compute - e.g., already visisted
# Check each location faster
    # More advanced caching, 

def find_num_locations(start, max_steps):
    current_positions = [start]
    all_positions = {(start, 0)}
    for _ in range(1, max_steps + 1):
        new_positions = set()
        while current_positions:
            pos = current_positions.pop()
            new_directions = get_new_directions(pos)
            new_positions.update(new_directions)
        else:
            current_positions = new_positions
    return current_positions


@cache
def shrink_to_original_map(pos):
    mapped_y = pos[0] % len(grid)
    mapped_x = pos[1] % len(grid[0])
    return mapped_y, mapped_x

@cache
def get_new_directions(pos):
    mapped_y, mapped_x = shrink_to_original_map(pos)
    available_directions = grid_map[(mapped_y, mapped_x)]
    new_directions = set([(pos[0] + dir[0], pos[1] + dir[1]) for dir in available_directions])
    return new_directions

def get_grid_map(grid, directions):
    grid_map = {}
    for row_num, row in enumerate(grid):
        for col_num, cell in enumerate(row):
            if grid[row_num][col_num] == "#":
                continue
            possible_directions = []
            for dir in directions:
                ny, nx = row_num + dir[0], col_num + dir[1]
                if (0 <= ny < len(grid)) and (0 <= nx < len(grid[0])):
                    if grid[ny][nx] != ".":
                        continue
                ny_normalized, nx_normalized = ny - row_num, nx - col_num
                possible_directions.append((ny_normalized, nx_normalized))

            grid_map[(row_num, col_num)] = possible_directions
    return grid_map


grid_map = get_grid_map(grid, directions)

#16 733 044

locations = set(find_num_locations(start_pos, 50))
print(len(locations))


