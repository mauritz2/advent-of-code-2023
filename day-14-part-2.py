import time
from functools import cmp_to_key

with open("day-14-data.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]
    round_stones = []
    square_stones = []
    num_rows = len(data)
    for row_num in range(len(data)):
        for col_num in range(len(data)):
            char = data[row_num][col_num]
            if char == "O":
                round_stones.append((row_num, col_num))
            elif char == "#":
                square_stones.append((row_num, col_num))

def rank_by_direction(round_stone_1, round_stone_2, direction):
    index_map = {'North': 0, 'South': 0, 'West': 1, 'East': 1}
    index = index_map[direction]

    if direction in ['North', 'West']:
        if round_stone_1[index] < round_stone_2[index]:
            return -1
        else:
            return 1
    else:
        if round_stone_1[index] < round_stone_2[index]:
            return 1
        else:
            return -1

start_time = time.time()

direction = 'North' 
round_rocks_by_direction = sorted(round_stones, key=cmp_to_key(lambda x, y: rank_by_direction(x, y, direction)))

new_round_rocks = []

for round_rock in round_rocks_by_direction:
    if direction == "North":
        if round_rock[0] == 0:
            new_round_rocks.append(round_rock)
            continue
        squares_and_circles = square_stones + new_round_rocks
        squares_and_circles_below = [stone for stone in squares_and_circles if stone[0] < round_rock[0] and stone[1] == round_rock[1]]
        #circles_below = [circle for circle in new_round_rocks if circle[0] < round_rock[0] and circle[1] == round_rock[1]]
        if squares_and_circles_below:
            new_row = max([pos[0] for pos in squares_and_circles_below]) + 1
        else:
            new_row = 0
        new_round_rocks.append((new_row, round_rock[1]))

end_time = time.time()
print((end_time - start_time) * 1000000000 / 60 / 60)

total_score = 0
for stone in new_round_rocks:
    total_score += (num_rows - stone[0])

print(total_score)
