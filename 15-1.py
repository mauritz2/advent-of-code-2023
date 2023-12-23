with open ("inputs/15.txt") as f:
    instructions = f.read().split(",")

def calc_hash(instruction:str) -> int:
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

sum_of_hash_values = 0

for instruction in instructions:
    sum_of_hash_values += calc_hash(instruction)

print(sum_of_hash_values)
