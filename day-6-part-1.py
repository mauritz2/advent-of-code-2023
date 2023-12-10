with open("day-6-data.txt") as f:
    data = f.readlines()
    time = list(map(int, data[0].strip().split()[1:]))
    distance = list(map(int, data[1].strip().split()[1:]))

total_won_races = 0
for (race_time, record) in zip(time, distance):
    print(race_time)
    print(record)
    
    for i in range(0, time + 1):
        speed = i
        distance = speed * (time - i)
        if distance > record:
            total_won_races += 1
print(total_won_races)
