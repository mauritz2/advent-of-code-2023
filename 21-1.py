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
            for dir in directions:
                ny, nx = pos[0] + dir[0], pos[1] + dir[1]
                if not (0 <= ny < len(grid)) or not (0 <= nx < len(grid[0])):
                    continue
                if grid[ny][nx] != ".":
                    continue
                if (ny, nx) in new_positions:
                    continue
                new_positions.append((ny, nx))
        else:
            current_positions = new_positions.copy()
    return current_positions

locations = find_num_locations(start_pos, 64, data)
print(len(set(locations)))

#for visited in locations:
#    data[visited[0]][visited[1]] = "O"
#for row in data:
#    print("".join(row))
