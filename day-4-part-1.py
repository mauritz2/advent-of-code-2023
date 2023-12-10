with open("day-4-data.txt") as f:
    data_raw = f.readlines()
    data = [row.strip() for row in data_raw]

scratch_cards = {i:1 for i in range(1, len(data) + 1)}

def calc_num_scratch_cards_won(card_num):
    total_matches = 0
    
    row = data[card_num - 1]
    card_num_end = row.find(":")
    winning_and_our_nums = row[card_num_end + 1:].split("|")
    winning = winning_and_our_nums[0].split()
    our_nums = winning_and_our_nums[1].split()

    for our_num in our_nums:
        if our_num in winning:
            total_matches += 1
    return total_matches

for card_num in range(1, len(data) + 1):
    num_scratches_won = calc_num_scratch_cards_won(card_num)
    for _ in range(scratch_cards[card_num]):
        for i in range(1, num_scratches_won + 1):
            if card_num + i in scratch_cards:
                scratch_cards[card_num + i] += 1

print(sum(scratch_cards.values()))
