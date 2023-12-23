import time
from collections import defaultdict
from functools import lru_cache

blocks_by_col = defaultdict(set)
blocks_by_row = defaultdict(set)

with open("day-14-data.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]
    round_stones = []
    square_stones = []
    num_rows = len(data)
    num_cols = len(data[0])
    for row_num in range(len(data)):
        for col_num in range(len(data)):
            char = data[row_num][col_num]
            if char == "O":
                round_stones.append((row_num, col_num))
            elif char == "#":
                square_stones.append((row_num, col_num))

        for square in square_stones:
            blocks_by_col[square[1]].add(square[0])
            blocks_by_row[square[0]].add(square[1])

new_round_stones = []

dir_mod = {
    "North": {"comp": lambda block, cur_stone: block < cur_stone, "nearest": max, "offset": 1, "max_pos":0, "block_dict":blocks_by_col},
    "West": {"comp": lambda block, cur_stone: block < cur_stone, "nearest": max, "offset": 1, "max_pos":0, "block_dict":blocks_by_row},
    "South": {"comp": lambda block, cur_stone: block > cur_stone, "nearest": min, "offset": -1, "max_pos":len(data), "block_dict":blocks_by_col},
    "East": {"comp": lambda block, cur_stone: block > cur_stone, "nearest": min, "offset": -1, "max_pos":len(data[0]), "block_dict":blocks_by_row}
}


#@lru_cache(maxsize=None)  
def tilt_board(round_stones, direction):
    new_round_rocks = []

    for round_stone in round_stones:
        blocks = dir_mod[direction]["block_dict"][round_stone[1]]
        nearest_blocks = [square for square in blocks if dir_mod[direction]["comp"](square, round_stone[0])]

        if nearest_blocks:
            nearest_free_space = dir_mod[direction]["nearest"](nearest_blocks) + dir_mod[direction]["offset"]
        else:
            nearest_free_space = dir_mod[direction]["max_pos"]

        new_pos = (nearest_free_space, round_stone[1])
        dir_mod[direction]["block_dict"][round_stone[1]].add(nearest_free_space)
        new_round_rocks.append(new_pos)

    return new_round_rocks

new_round_stones = round_stones

for _ in range(1):
    new_round_stones = tilt_board(new_round_stones, direction="North")
    #new_round_rocks = tilt_board(new_round_rocks, blocks_by_col, direction="West")
    #new_round_rocks = tilt_board(new_round_rocks, blocks_by_col, direction="South")
    #new_round_rocks = tilt_board(new_round_rocks, blocks_by_col, direction="East")
    print(_)

total_score = 0
for stone in new_round_stones:
    total_score += (num_rows - stone[0])

print(total_score)
