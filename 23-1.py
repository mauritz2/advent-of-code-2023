with open("inputs/23.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]

start = (0, 1)
end = (len(data) - 1, len(data[0]) - 2)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Is this needed? Risk otherwise is that you end up in a deadend where only allowed step is backwards
allowed_approaches_by_hill = {
    "<": [(1,0), (-1,0), (0,1)],
    ">": [(1,0), (-1,0), (0,-1)],
    "^": [(0,1), (0,-1), (-1,0)],
    "v": [(0,1), (0,-1), (1,0)],
}

slide_directions = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

def get_next_steps(path, consider_slopes=False):
    next_steps = []
    last_step = path[-1]
    current_tile = data[last_step[0]][last_step[1]]
    if current_tile in slide_directions.keys():
        # If you are on a slider square your next step is required
        slide_step = slide_directions[current_tile]
        ny, nx = (last_step[0] + slide_step[0], last_step[1] + slide_step[1])
        if (ny, nx) in path:
            return next_steps
        else:
            return [(ny, nx)]

    for d in directions:
        ny, nx = (last_step[0] + d[0], last_step[1] + d[1])
        n_tile = data[ny][nx]
        if not 0 <= ny < len(data) or not 0 <= nx < len(data[0]):
            # Check if redundant since map is surrounded by trees
            continue
        if (ny, nx) in path:
            continue
        if n_tile == "#":
            continue
        #if n_tile in allowed_approaches_by_hill.keys():
            # Check if redundant since you will go on slide and then have a way back
        #    if d not in allowed_approaches_by_hill[n_tile]:
        #        continue
        next_steps.append((ny, nx))        
    return next_steps

complete_paths = []
paths_in_progress = [[start]]

while paths_in_progress:
    # What will happen in a dead end?
    path = paths_in_progress.pop()
    next_steps = get_next_steps(path)
    for step in next_steps:
        new_path = path.copy()  # Make a copy of the current path
        new_path.append(step)  # Append the new step to the copied path
        if step == end:
            complete_paths.append(new_path)
        else:
            paths_in_progress.append(new_path)
            #print(path)
            # (11, 21) --> Why doesn't it find (12, 21)?

longest_path = max([len(path) - 1 for path in complete_paths])
#print(len(complete_paths[0]))
print(longest_path)
print(len(complete_paths))
quit()
vis_data = [] 
for row in data:
    vis_data.append([c for c in row])
for step in complete_paths[0]:
    vis_data[step[0]][step[1]] = "O"
for row in vis_data:
    print("".join(row))

print()
