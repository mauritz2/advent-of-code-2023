with open("day-4-data.txt") as f:
    data_raw = f.readlines()
    data = [row.strip() for row in data_raw]

total_score = 0

for row in data:
    card_num_end = row.find(":")
    winning_and_our_nums = row[card_num_end + 1:].split("|")
    winning = winning_and_our_nums[0].split()
    our_nums = winning_and_our_nums[1].split()

    row_score = 0

    for our_num in our_nums:
        if our_num in winning:
            if row_score == 0:
                row_score = 1
            else:
                row_score *= 2
    total_score += row_score

print(total_score)
