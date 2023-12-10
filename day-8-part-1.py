
with open ("day-8-data.txt") as f:
    data_raw = f.readlines()
    data_raw = [row.strip() for row in data_raw]

    instructions = data_raw[0]    
    nodes = {}
    for row in data_raw[2:]:
        elements = row.split()
        node_name = elements[0]
        left = elements[2][1:-1]
        right = elements[3][:-1]
        nodes[node_name] = [left, right]

instruction_map = {
    "L":0,
    "R":1
}

current_node = "AAA"
step_count = 0

# Loop instructions
for _ in range(100):
    for char in instructions:
        current_node = nodes[current_node][instruction_map[char]]
        step_count +=1

        if current_node == "ZZZ":
            print(step_count)
            quit()
    