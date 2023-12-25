import ast 

def parse_part(part):
    part = part.replace("=", ":")
    for attribute in "xmas":
        pos = part.find(attribute)
        part = f"{part[:pos]}'{part[pos]}'{part[pos + 1:]}"
    part = ast.literal_eval(part)
    return part

def parse_instruction(instruction):
    parsed_operations = []
    operation_start = instruction.find("{")
    name = instruction[:operation_start]

    operations = instruction[operation_start + 1:-1].split(",")
    default_outcome = operations[-1]
    for operation in operations[:-1]:
        o, r = operation.split(":")
        parsed_operations.append((o, r))
    parsed_operations.append(("True", default_outcome))
    return name, parsed_operations
    

with open("inputs/19.txt") as f:
    raw_instructions, parts = f.read().split("\n\n")
    instructions = {}
    parts = list(map(parse_part, parts.split("\n")))
    for i in raw_instructions.split("\n"):
        name, operations = parse_instruction(i)
        instructions[name] = operations


def get_next_instruction(part, instruction):
    x, m, a, s = part["x"], part["m"], part["a"], part["s"]
    for operation in instruction:
        if eval(operation[0]):
            return operation[1]
    raise ValueError("At least one instruction should always be true")


total = 0

for part in parts:
    accepted = False
    instruction = instructions["in"]
    while True:    
        instruction_name = get_next_instruction(part, instruction)
        if instruction_name == "A":
            accepted = True
            break
        elif instruction_name == "R":
            break
        else:
            instruction = instructions[instruction_name]
    if accepted:
        x, m, a, s = part["x"], part["m"], part["a"], part["s"]
        total += x + m + a + s
print(total)