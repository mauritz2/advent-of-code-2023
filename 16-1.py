with open("inputs/16.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]

directions = {
    "N":(-1, 0),
    "S":(1, 0),
    "E":(0, 1),
    "W":(0, -1),
}

def get_new_direction(tile:str, direction:str) -> str:
    if tile == ".":
        new_direction = direction
    elif tile == "/":
        match direction:
            case "N":
                new_direction = "E"
            case "S":
                new_direction = "W"
            case "E":
                new_direction = "N"
            case "W":
                new_direction = "S"
    elif tile == "\\":
        match direction:
            case "N":
                new_direction = "W"
            case "S":
                new_direction = "E"
            case "E":
                new_direction = "S"
            case "W":
                new_direction = "N"
    else:
         new_direction = direction

    return new_direction

lighted_squares = []

start = ((0, 0), "E")
beams_to_extend = []
beams_to_extend.append(start)

matrix = [["."] * len(data[0]) for _ in range(len(data))]

seen = []

while beams_to_extend:
    next_beam = beams_to_extend.pop()
    x, y = next_beam[0][1], next_beam[0][0]
    direction = next_beam[1]

    if y < 0 or y >= len(data) or x < 0 or x >= len(data[0]):
        continue
    if next_beam in seen:
        continue

    seen.append(next_beam)
    lighted_squares.append((y, x))

    tiles = []
    current_tile = data[y][x]
    if (current_tile == "|" and direction in "EW") or (current_tile == "-" and direction in "NS"):
       tiles.append("\\")
       tiles.append("/")
    else:
       tiles.append(current_tile)
            
    for tile in tiles:
        new_direction = get_new_direction(tile, direction)
        new_y, new_x = [num_1 + num_2 for num_1, num_2 in zip(next_beam[0], directions[new_direction])]
        beams_to_extend.append(((new_y, new_x), new_direction))

print(len(set(lighted_squares)))

for light_square in lighted_squares:
    x, y = light_square[1], light_square[0]
    matrix[y][x] = "#"
for r in matrix:
    print("".join(r))

