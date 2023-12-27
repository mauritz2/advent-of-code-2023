# From u/msschmitt

#!/usr/bin/env python3
# 2023 Day 21: Step Counter

from collections import deque

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    garden = {}

    x_len = len(input[0])
    y_len = len(input)

    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            garden[(x,y)] = ch
            if ch == 'S':
                start = (x,y)

    return garden, start, x_len, y_len

def take_steps(step_limit):
    stepped_to = set()
    stepped_to.add(start)

    for s in range(step_limit):
        stepped_to = take_a_step(stepped_to)
    return stepped_to

def take_a_step(from_steps):
    to_steps = set()
    for pos in from_steps:
        for dir in 'NWES':
            new_pos = adjust_pos(pos, dir)
            if garden_ch(new_pos) == '#':      # rock
                continue
            to_steps.add(new_pos)
    return to_steps

def adjust_pos(coord, dir):
    x, y = coord
    adjust = {'E':(1,0), 'W':(-1,0), 'S':(0,1), 'N':(0,-1)}
    ax, ay = adjust[dir]
    x += ax
    y += ay
    return (x, y)

def garden_ch(coord):
    x, y = coord
    a = x % x_len
    b = y % y_len
    ch = garden[(a,b)]
    return ch


def analyze_result():
    print('Analyzing for N =',n)
    print('Total plots reached:',len(plots_reached))
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for x, y in plots_reached:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    squares = int((max_x - min_x + 1) / x_len)
    print('Area reached is',squares,'x',squares)

    square_totals = []
    x = min_x
    y = min_y
    for a in range(squares):        # down
        row = []
        for b in range(squares):    # across
            plots = 0
            for x1 in range(x,x+x_len):
                for y1 in range(y,y+y_len):
                    if (x1, y1) in plots_reached:
                        plots += 1
            row.append(plots)
            x += x_len
        square_totals.append(row)
        x = min_x
        y += y_len
    return square_totals


def calculate_plots():
    plots = 0

    full_odd = squares[2][2]
    full_even = squares[2][1]
    s1 = squares[0][1] + squares[0][3] + squares[4][1] + squares[4][3]
    s2 = squares[0][2] + squares[2][0] + squares[2][4] + squares[4][2]
    s3 = squares[1][1] + squares[1][3] + squares[3][1] + squares[3][3]

    plots = (s1 * n) + s2 + (s3 * (n-1)) + (full_even * n**2) + (full_odd * (n-1)**2)
    return plots

#-----------------------------------------------------------------------------------------

filename = 'inputs/day21.txt'

garden, start, x_len, y_len = process_input(filename)

garden_width = x_len
half_width = int((x_len - 1)/2)

# Analyze results with N=2...
print()
print('Taking steps...')
n = 2
plots_reached = take_steps(half_width + garden_width * n)
squares = analyze_result()

print()
for s in squares:
    print(s)
print()

target_steps = 26501365
n = int((target_steps - half_width) / garden_width)
print('Answer requires N =',n)

final_plots = calculate_plots()

print()
print('Plots reached: ', final_plots)