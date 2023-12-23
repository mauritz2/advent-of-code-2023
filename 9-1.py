with open("day-9-data.txt") as f:
    data_raw = f.readlines()
    data = []
    for row in data_raw:
        data.append(list(map(int, row.split())))

def calc_row_diff(row:list[int]) -> list[int]:
    differences = []
    for i in range(len(row) - 1):
        differences.append(row[i + 1] - row[i])
    assert((len(differences) + 1 == len(row))) 
    return differences

sum_of_prediction = 0
for row in data:
    found_bottom_row = False
    all_rows = []
    all_rows.append(row)
    next_row = row
    while found_bottom_row is False:
        next_row = calc_row_diff(next_row)
        all_rows.append(next_row)
        if all([num == 0 for num in next_row]):
            found_bottom_row = True
    row_prediction = 0
    for row in all_rows:
        print(row)
        row_prediction += row[0]
        print(row_prediction)
    sum_of_prediction += row_prediction

print(sum_of_prediction)