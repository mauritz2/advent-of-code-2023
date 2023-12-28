from collections import namedtuple

LinearEquation = namedtuple("LinearEquation", ["y", "k", "x", "m", "x_vel", "y_vel"])

def linear_equation(row: str) -> LinearEquation:
    position, velocity = row.split("@")
    x_pos, y_pos, _ = [int(num) for num in position.split(",")]
    x_vel, y_vel, _ = [int(num) for num in velocity.split(",")]
    k = y_vel / x_vel    
    m = y_pos - (k * x_pos)
    return LinearEquation(y_pos, k, x_pos, m, x_vel, y_vel)


def will_collide(pair):
    min_boundary = 200000000000000 
    max_boundary = 400000000000000
    hail1, hail2 = pair[0], pair[1]
    if hail1.k != hail2.k:
        x_intersect = (hail2.m - hail1.m) / (hail1.k - hail2.k)
        y_intersect = hail1.k * x_intersect + hail1.m

        if min_boundary <= x_intersect <= max_boundary and min_boundary <= y_intersect <= max_boundary:
            future_path_hail1 = (x_intersect >= hail1.x) if hail1.x_vel > 0 else (x_intersect <= hail1.x)
            future_path_hail2 = (x_intersect >= hail2.x) if hail2.x_vel > 0 else (x_intersect <= hail2.x)
            if future_path_hail1 and future_path_hail2:
                return 1
    return 0

linear_equations = []
with open("inputs/day24.txt") as f:
    data = f.readlines()
    data = [row.strip() for row in data]
    linear_equations = list(map(linear_equation, data))

pairs = []
for i, l1 in enumerate(linear_equations):
    for l2 in linear_equations[i + 1:]:
        pairs.append((l1, l2))

total_collisions = sum(list(map(will_collide, pairs)))
print(total_collisions)