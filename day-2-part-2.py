import re 

with open("day-2-data.txt") as f:
    data_raw = f.readlines()
    data = [row.strip() for row in data_raw]

game_id_pattern = re.compile(r"[0-9]{1,3}")
# Can be combined into one expression to match all colors in a single expression with matching groups
blue_pattern = re.compile(r"([0-9]+)(?: blue)")
green_pattern = re.compile(r"([0-9]+)(?: green)")
red_pattern = re.compile(r"([0-9]+)(?: red)")

total_power = 0

for row in data:
    game_id_end = row.find(":")
    game_id = int(re.search(game_id_pattern, row[:game_id_end]).group(0))

    games_str = row[game_id_end + 1:]
    games = games_str.split(";")

    min_blue = 0
    min_green = 0
    min_red = 0

    # Can be simplified, lots of repetition
    for game in games:
        blue_num = blue_pattern.search(game)
        green_num = green_pattern.search(game)
        red_num = red_pattern.search(game)

        if blue_num:
            if int(blue_num.group(1)) > min_blue:
                min_blue = int(blue_num.group(1))  
        if green_num:
            if int(green_num.group(1)) > min_green:
                min_green = int(green_num.group(1))
        if red_num:
            if int(red_num.group(1)) > min_red:
                min_red = int(red_num.group(1))        
    else:
        power = min_blue * min_green * min_red
        total_power += power
        
print(total_power)