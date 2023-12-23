from itertools import combinations_with_replacement

with open("inputs/17.txt") as f:
    data = f.readlines()
    data = [[int(char) for char in row.strip()] for row in data]

directions = {
    "up":(-1, 0),
    "down":(1, 0),
    "left":(0, -1),
    "right":(0, 1)
}
opposites = {
    "left":"right",
    "right":"left",
    "up":"down",
    "down":"up"
}
direction = "right"
position = (0,0)

while position != (13, 13):
    
    allowed_directions = [d for d in directions.keys() if d != opposites[direction]]
    # Does not allow for a u turn! Maybe not needed since it's redundant anyways
    step_combinations = [[directions[s] for s in step] for step in list(combinations_with_replacement(allowed_directions, 3))]
    #step_combinations = [[(0,1),(1,0),(0,1)]]

    least_heat = 100
    for steps in step_combinations:
        heat_loss = 0 
        valid_steps = True
        position = (0, 0)
        heats_taken = []
        heat_at_step = None
        for step in steps:
            position = (step[0] + position[0], step[1] + position[1]) 
            if (position[0] < 0 or position[0] >= len(data)) or (position[1] < 0 or position[1] >= len(data[0])):
                valid_steps = False
                break
            heat_at_step = data[position[0]][position[1]]
            heats_taken.append(heat_at_step)
            heat_loss += heat_at_step
        if valid_steps:
            if (heat_loss < least_heat):
                least_heat = heat_loss
                best_end = 
                print(heats_taken)
                print(least_heat)
                print("###")
    print(least_heat)