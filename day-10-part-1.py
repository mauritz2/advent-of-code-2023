
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

def get_pipe_direction(current_pos:tuple[int], current_pipe_type:str, previous_pos:tuple[int]) -> tuple[int]:
    #print(current_pipe_type)
    pipe_exit_options = pipe_directions[current_pipe_type]
    if add_tuple(pipe_exit_options[0], current_pos) == previous_pos:
        pipe_exit_direction = pipe_exit_options[1]
    else:
        pipe_exit_direction = pipe_exit_options[0]
    
    return pipe_exit_direction

start_pos = find_animal_start(data)
potential_loops = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#potential_loops = [(1, 0)]

the_loop = []

for p_l in potential_loops:
    the_loop.append(start_pos)
    previous_pos = start_pos
    current_pos = add_tuple(start_pos, p_l)
    continue_loop_search = True

    while continue_loop_search:
        current_pipe_type = data[current_pos[0]][current_pos[1]]
        #print(current_pipe_type)
        if pipe_directions[current_pipe_type] is None:
            the_loop = []
            continue_loop_search = False
        else:
            pipe_exit_direction = get_pipe_direction(current_pos, current_pipe_type, previous_pos) 
            
            previous_pos = current_pos
            current_pos = add_tuple(current_pos, pipe_exit_direction)
            if current_pos == the_loop[0]:
                continue_loop_search = False
            
            the_loop.append(previous_pos)
    else:
        print(the_loop)
        break

                