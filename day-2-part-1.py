import re 

with open("day-2-data.txt") as f:
    data_raw = f.readlines()
    data = [row.strip() for row in data_raw]

game_id_pattern = re.compile(r"[0-9]{1,3}")
blue_pattern = re.compile(r"([0-9]+)(?: blue)")
green_pattern = re.compile(r"([0-9]+)(?: green)")
red_pattern = re.compile(r"([0-9]+)(?: red)")

MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12

sum_impossible_ids = 0

for row in data:
    game_id_end = row.find(":")
    game_id = int(re.search(game_id_pattern, row[:game_id_end]).group(0))

    games_str = row[game_id_end + 1:]
    games = games_str.split(";")

    for game in games:
        blue_num = blue_pattern.search(game)
        green_num = green_pattern.search(game)
        red_num = red_pattern.search(game)

        if blue_num:
            if int(blue_num.group(1)) > MAX_BLUE:
                break        
        if green_num:
            if int(green_num.group(1)) > MAX_GREEN:
                break        
        if red_num:
            if int(red_num.group(1)) > MAX_RED:
                break
        
    else:
        print(f"{game_id} is possible")
        sum_impossible_ids += game_id
        
print(sum_impossible_ids)