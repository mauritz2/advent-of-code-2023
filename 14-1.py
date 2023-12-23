import time

# Start timing
start_time = time.time()
with open("day-14-data.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]

total_weight = 0
row_len = len(data)

for row_num, row in enumerate(data):
    for col_num in range(len(data[0])):
        if data[row_num][col_num] != "O":
            continue
        northern_positions = [pos[col_num] for pos in data[:row_num]][::-1]
        northernmost_pos = row_num
        if northern_positions:
            for pos in northern_positions:
                if pos == ".":
                    northernmost_pos -= 1
                else:
                     break
        data[row_num] = data[row_num][:col_num] + "." + data[row_num][col_num + 1:]
        data[northernmost_pos] = data[northernmost_pos][:col_num] + "O" + data[northernmost_pos][col_num + 1:]
        total_weight += (row_len - northernmost_pos)

print(total_weight)

print((time.time() - start_time) * 1000000000 / 60 / 60)