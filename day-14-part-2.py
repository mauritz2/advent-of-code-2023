import time

# Start timing
with open("day-14-data.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]

#total_weight = 0
row_len = len(data)

# It would be better to just keep track of the locations instead
# 

start_time = time.time()

def roll_balls(platform, direction):
    total_weight = 0
    for row_num, row in enumerate(platform):
        for col_num in range(len(platform[0])):
            if platform[row_num][col_num] != "O":
                continue
            northern_positions = [pos[col_num] for pos in platform[:row_num]][::-1]
            northernmost_pos = row_num
            if northern_positions:
                for pos in northern_positions:
                    if pos == ".":
                        northernmost_pos -= 1
                    else:
                        break
            platform[row_num] = platform[row_num][:col_num] + "." + platform[row_num][col_num + 1:]
            platform[northernmost_pos] = platform[northernmost_pos][:col_num] + "O" + platform[northernmost_pos][col_num + 1:]
            total_weight += (row_len - northernmost_pos)
    else:
        return total_weight

total_weight = roll_balls(data, "")
print(total_weight)

# 38. 67
# 33.37 (when not looping through everything - but still looking at everything below)
# 16 - now that we have a hashmap for closest block
print((time.time() - start_time) * 1000000000 * 4 / 60 / 60)