from collections import defaultdict

with open ("inputs/15.txt") as f:
    instructions = f.read().split(",")

def calc_label(instruction:str) -> int:
    total_value = 0
    for char in instruction:
        #Determine the ASCII code for the current character of the string.
        ascii_val = ord(char)
        #Increase the current value by the ASCII code you just determined.
        total_value += ascii_val
        #Set the current value to itself multiplied by 17.
        total_value *= 17
        #Set the current value to the remainder of dividing itself by 256.
        total_value %= 256
    return total_value

boxes = defaultdict(list)

for instruction in instructions:
    equals_pos = instruction.find("=")
    hyphen_pos = instruction.find("-")

    label_end = equals_pos if equals_pos != -1 else hyphen_pos
    lens_name = instruction[:label_end]
    box_num = calc_label(lens_name)
    operation = instruction[equals_pos] if equals_pos != -1 else instruction[hyphen_pos]

    if operation == "=":
        focal_length = instruction[-1]
        lens_name_and_focal = f"{lens_name} {focal_length}"

        for i, lens in enumerate(boxes[box_num]):
            if lens_name in lens:
                boxes[box_num][i] = lens_name_and_focal
                break
        else:
            boxes[box_num].append(lens_name_and_focal)
    
    elif operation == "-":
        for i, lens in enumerate(boxes[box_num]):
            if lens_name in lens:
                boxes[box_num].pop(i)
                break

total_value = 0

for key, value in boxes.items():
    box_value = int(key) + 1
    for i, lens in enumerate(value):
        total_value += box_value * int(lens[-1]) * (i + 1)

print(total_value)