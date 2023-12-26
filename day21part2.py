with open("inputs/day21.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]
    start_pos = None
    for i, row in enumerate(data):
        s_pos = row.find("S")
        if s_pos != -1:
            start_pos = (i, s_pos)
            break
    data = [[c for c in row] for row in data]
    data[start_pos[0]][start_pos[1]] = "."

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def find_num_locations(start, max_steps, grid):
    current_positions = [start]
    for step_num in range(1, max_steps + 1):
        new_positions = []
        while current_positions:
            pos = current_positions.pop()
            # map_x, map_y = pos thing (get mapped coords)
            # new_locs = dict[(map_y, map_x)]
            # new_positions.extend(new_locs)
        else:
            current_positions = new_positions.copy()
    return current_positions

# {(1, 0): [(1, 0), (0, 1)] 
# How do you deal with the expanding ones?
# Map the expanding squares to the main dict
# Coordinates are y, x
# But we need to find map_y, map_x
# map_x % len(grid[0])

# for dir in directions:
#     ny, nx = pos[0] + dir[0], pos[1] + dir[1]
#     if not (0 <= ny < len(grid)) or not (0 <= nx < len(grid[0])):
#         continue
#     if grid[ny][nx] != ".":
#         continue
#     if (ny, nx) in new_positions:
#         continue

locations = find_num_locations(start_pos, 26501365, data)
print(len(set(locations)))

#for visited in locations:
#    data[visited[0]][visited[1]] = "O"
#for row in data:
#    print("".join(row))


