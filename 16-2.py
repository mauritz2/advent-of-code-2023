from functools import cache

with open("inputs/16.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]

directions = {
    "N":(-1, 0),
    "S":(1, 0),
    "E":(0, 1),
    "W":(0, -1),
}

@cache
def get_new_direction(tile:str, direction:str) -> str:
    if tile == "/":
        new_direction = {"N":"E", "S":"W", "E":"N","W":"S"}[direction]
    elif tile == "\\":
        new_direction = {"N":"W", "S":"E", "E":"S","W":"N"}[direction]
    else:
         new_direction = direction
    return new_direction

@cache
def get_next_loc(current_loc:tuple[int], adjustment:tuple[int]) -> tuple[int]:
    return [num_1 + num_2 for num_1, num_2 in zip(current_loc, adjustment)]

def get_starts():
    num_rows, num_cols = len(data), len(data[0])
    top_starts = [((0, x), "S") for x in range(num_cols)]
    bottom_starts = [((num_rows - 1, x), "N") for x in range(num_cols)]
    right_starts = [((x, num_cols - 1), "W") for x in range(num_rows)]
    left_starts = [((x, 0), "E") for x in range(num_rows)]
    starts = top_starts + bottom_starts + right_starts + left_starts
    return starts

top_lighted_squares = 0

for start in get_starts():
    lighted_squares = []
    seen = []
    beams_to_extend = []
    beams_to_extend.append(start)

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
            new_y, new_x = get_next_loc(next_beam[0], directions[new_direction])
            beams_to_extend.append(((new_y, new_x), new_direction))
    if len(set(lighted_squares)) > top_lighted_squares:
        top_lighted_squares = len(set(lighted_squares))

print(top_lighted_squares)