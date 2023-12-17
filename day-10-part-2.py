import math

with open("day-10-data.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]

    # Pad data to avoid index out of range checking
    target_len = len(data[0]) + 2
    data = [line.center(target_len, '.') for line in data]
    dot_row = '.' * target_len
    data.insert(0, dot_row)
    data.append(dot_row)

pipe_directions = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": None
}

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

def add_tuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def find_animal_start(pipes:list[str]) -> tuple[int]:
    row = 0
    col = 0
    for row_num in range(len(pipes)):
        if "S" in pipes[row_num]:
            row = row_num
            col = pipes[row_num].find("S")
    return (row, col)

def get_pipe_direction(current_pos:tuple[int], current_pipe_type:str, loop_path:list[tuple[int]]) -> tuple[int]:
    pipe_exit_options = pipe_directions[current_pipe_type]
    if add_tuple(pipe_exit_options[0], current_pos) in loop_path[1:]:
        pipe_exit_direction = pipe_exit_options[1]
    else:
        pipe_exit_direction = pipe_exit_options[0]
  
    return pipe_exit_direction

start_pos = find_animal_start(data)
potential_loops = [(1, 0)]
loop_path = []

for p_l in potential_loops:
    loop_path.append(start_pos)
    current_pos = add_tuple(start_pos, p_l)
    continue_loop_search = True

    while continue_loop_search:

        current_pipe_type = data[current_pos[0]][current_pos[1]]
        if current_pipe_type == ".":
            loop_path = []
            continue_loop_search = False
        
        elif current_pos == loop_path[0]:
            #print(f"The complete loop has been found at {loop_path}")
            continue_loop_search = False

        else:
            loop_path.append(current_pos)
            pipe_exit_direction = get_pipe_direction(current_pos, current_pipe_type, loop_path)             
            current_pos = add_tuple(current_pos, pipe_exit_direction)
    else:
        max_distance_from_start =  math.ceil(len(loop_path) / 2)
        print(f"Max distance from start is {max_distance_from_start}")
        break

# Part 2 solution adopted from u/hi_im_new_to_this
# Loop through all locations and shoot a diagonal ray towards bottom-right
# If the ray crosses the main loop pipe an odd number of times it means it's on the inside
data[start_pos[0]] = data[start_pos[0]].replace("S" , "|")

inside_count = 0
inside_locs = []
grid_width = len(data[0])
grid_height = len(data)
for y_start, row_data in enumerate(data):
    for x_start, col_data in enumerate(row_data):
        if (y_start, x_start) in loop_path:
            # Part of the loop pipes - continue
            continue
        
        times_crossed_pipe = 0
        x2, y2 = x_start, y_start

        while x2 < grid_width and y2 < grid_height:
            c2 = data[y2][x2]
            if (y2, x2) in loop_path and c2 != "L" and c2 != "7":
                times_crossed_pipe += 1
            x2 += 1
            y2 += 1

        if times_crossed_pipe % 2 == 1:
            inside_locs.append((y_start, x_start))
            inside_count += 1

print(f"Part 2: {inside_count}")
# Visualize the locations that are within the loop
for y_start, row_data in enumerate(data):
    for x_start, col_data in enumerate(row_data):
        if (y_start, x_start) in inside_locs:
            original_string = data[y_start]
            new_string = original_string[:x_start] + "O" + original_string[x_start + 1:]
            data[y_start] = new_string
                
    print(data[y_start])
