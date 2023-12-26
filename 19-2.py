import copy
from functools import reduce

# Min inclusive, max exclusive
# Max amount of combos: 256,000,000,000,000
default_part_range = {
    "x":[1, 4000],
    "m":[1, 4000],
    "a":[1, 4000],
    "s":[1, 4000]
    }

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

passing_ranges = []
def append_passing_ranges(part_range, instruction_name, instructions):
        if instruction_name == "R":
            return
        elif instruction_name == "A":
            passing_ranges.append(part_range)
            return 

        instruction = instructions[instruction_name]
        passing_part_range = copy.deepcopy(part_range)
        failing_part_range = copy.deepcopy(part_range)

        for operation in instruction:
            if operation[0] == "True":
                append_passing_ranges(part_range, operation[1], instructions)
                break

            attribute = operation[0][0]
            operation_sign = operation[0][1]
            if operation_sign == ">":
                new_min = int(operation[0][2:])
                if part_range[attribute][0] < new_min:
                    if new_min < part_range[attribute][1]:
                        passing_part_range[attribute][0] = new_min + 1
                        failing_part_range[attribute][1] = new_min
                    else:
                        passing_part_range[attribute][0] = 0
                        passing_part_range[attribute][1] = 0

            if operation_sign == "<":
                new_max = int(operation[0][2:])
                if part_range[attribute][1] > new_max:
                    if part_range[attribute][0] < new_max:
                        passing_part_range[attribute][1] = new_max - 1
                        failing_part_range[attribute][0] = new_max
                    else:
                        passing_part_range[attribute][0] = 0
                        passing_part_range[attribute][1] = 0
                        #passing_part_range[attribute][0] = 0
            

            assert passing_part_range[attribute][0] <= passing_part_range[attribute][1]
            assert failing_part_range[attribute][0] <= failing_part_range[attribute][1]
            # The part that passes the operation --> Change the instruction
            part_range = failing_part_range
            append_passing_ranges(passing_part_range, operation[1], instructions)
            #get_passing_parts(failing_part_range, operation)
        #print(original_part_range)           
        #print(passing_part_range)           
        #print(failing_part_range)           
        #get_passing_parts(part_range) 
def get_instructions(raw_instructions):
    instructions = {}
    for i in raw_instructions.split("\n"):
        name, operations = parse_instruction(i)
        instructions[name] = operations
    return instructions

def test_1():
    data ="""\
in{s<1351:px,qqz}
px{a<2006:A,R}
qqz{s>2770:R,R}"""
    instructions = get_instructions(data)
    append_passing_ranges(default_part_range, "in", instructions)
    assert passing_ranges == [{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 2005], 's': [1, 1350]}]

def test_2():
    data ="""\
in{s<1351:px,qqz}
px{a<2006:A,R}
qqz{s>2770:A,R}"""
    instructions = get_instructions(data)
    append_passing_ranges(default_part_range, "in", instructions)
    assert passing_ranges == [{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 2005], 's': [1, 1350]}, {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [2771, 4000]}]

def test_3():
    data ="""\
in{s<1351:A,A}"""
    instructions = get_instructions(data)
    append_passing_ranges(default_part_range, "in", instructions)
    assert passing_ranges == [{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 1350]}, {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1351, 4000]}]

def count_range(a, b):
    return a * b 

def tests():
    #test_1()
    #test_2()
    #test_3()
    pass


def main():
    with open("inputs/19.txt") as f:
        raw_instructions, _ = f.read().split("\n\n")
    instructions = get_instructions(raw_instructions)
    append_passing_ranges(default_part_range, "in", instructions)
    
    total_count = 0
    ranges = [[range[1] - range[0] + 1 for range in range_dict.values()] for range_dict in passing_ranges]
    for range in ranges:
        total_count += reduce(lambda a, b: a * b, range)
    print(total_count)
    #163 494 853 788 000
    #167 409 079 868 000
main()
