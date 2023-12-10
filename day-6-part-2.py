import math 
from matplotlib import pyplot as plt

with open("day-6-data.txt") as f:
    data = f.readlines()
    race_time = data[0].strip().split()[1:]
    race_time = int("".join(race_time))
    race_record = data[1].strip().split()[1:]
    race_record = int("".join(race_record))

def solve_quadratic_for_y(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    sol1 = (-b + d) / (2*a)
    sol2 = (-b - d) / (2*a)
    return sol1, sol2

y = race_record  # You can change this value to whatever y value you need
a, b, c = -1, race_time, -y
solutions = solve_quadratic_for_y(a, b, c)
print(f"The solutions for x are {solutions[0]} and {solutions[1]}")
print(f"The answer is {int(solutions[1] - solutions[0])}")

### 

def plotting():
    charge_time = []
    distance_traveled = []
    for i in range(race_time):
        charge_time.append(i) 
        distance_traveled.append(i * (race_time - i))

    fig, ax = plt.subplots()
    ax.plot(charge_time, distance_traveled)
    ax.hlines(y=distance_traveled, xmin=0, xmax=max(charge_time), linewidth=2, color='r')
    plt.show()

def brute_force():
    ways_to_win_race = 0
    for i in range(0, race_time + 1):
        speed = i
        distance = speed * (race_time - i)
        if distance > race_record:
            print(distance)
            ways_to_win_race += 1

    print(ways_to_win_race)
    
