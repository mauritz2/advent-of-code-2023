import math 

with open("day-6-data.txt") as f:
    data = f.readlines()
    time = list(map(int, data[0].strip().split()[1:]))
    distance = list(map(int, data[1].strip().split()[1:]))

total_ways_to_win = []

for (race_time, record) in zip(time, distance):
    ways_to_win_race = 0
    
    for i in range(0, race_time + 1):
        # 8
        # 
        speed = i
        distance = speed * (race_time - i)
        if distance > record:
            print(distance)
            ways_to_win_race += 1

    total_ways_to_win.append(ways_to_win_race)
    
print(math.prod(total_ways_to_win))