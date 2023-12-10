from functools import cmp_to_key

with open("day-7-data.txt") as f:
    data_raw = f.readlines()
    data = [row.strip() for row in data_raw]

    hands = []
    bets = {}
    for row in data:
        hand, bet = row.split()
        if hand in bets:
            raise ValueError("All hands need to be unique")
        bets[hand] = int(bet)
        hands.append(hand)

card_to_val = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

def set_jokers(hand_dict):
    if "J" not in hand_dict:
        # Nothing to optimize
        return hand_dict
    
    num_jokers = hand_dict["J"]
    if num_jokers == 5:
        # Already optimized
        return hand_dict

    del hand_dict["J"]
    most_common_card = max(hand_dict, key=hand_dict.get)
    hand_dict[most_common_card] += num_jokers

    return hand_dict

def get_primary_rank(hand:str) -> int:
    hand_dict = {}

    for card in hand:
        if card not in hand_dict.keys():
            hand_dict[card] = 1
        else:
            hand_dict[card] += 1

    # Optimize the hand by converting Jokers
    hand_dict = set_jokers(hand_dict)

    hand_values = hand_dict.values()
    
    if 5 in hand_values:
        hand_rank = 1
    elif 4 in hand_values:
        hand_rank = 2
    elif (3 in hand_values) and (2 in hand_values):
        hand_rank = 3
    elif 3 in hand_values:
        hand_rank = 4
    elif sorted(hand_values) == [1, 2, 2]:
        hand_rank = 5
    elif 2 in hand_values:
        hand_rank = 6
    else:
        hand_rank = 7
    return hand_rank

def compare_hands(hand1:str, hand2:str) -> bool:
    # Compatationally expensive to call these each time each time a comparison happens
    # but runs fine in part one at least
    hand1_rank = get_primary_rank(hand1)
    hand2_rank = get_primary_rank(hand2)

    if hand1_rank < hand2_rank:
        return -1
    elif hand2_rank < hand1_rank:
        return 1

    for card1, card2 in zip(hand1, hand2):
        if card_to_val[card1] > card_to_val[card2]:
            return -1
        elif card_to_val[card2] > card_to_val[card1]:
            return 1
    else:
        raise NotImplemented("Case of perfect ties not covered")
    
sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))
sorted_hands.reverse()

sum_of_bets = 0
for rank, hand in enumerate(sorted_hands):
    bid = bets[hand] * (rank + 1)
    sum_of_bets += bid

print(sum_of_bets)
    

