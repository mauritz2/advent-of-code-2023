# By u/i_have_no_biscuits
def decode1(lines):
    return [(d, int(n)) for d, n, _ in lines]

def decode2(lines):
    return [("RDLU"[int(h[7])], int(h[2:7], 16)) for _, _, h in lines]

def find_area(instructions):
    perimeter, shoelace = 0, 0
    x, y, pts = 0, 0, [(0,0)]
    for d, n in instructions:
        dx, dy = {"R":(1, 0), "L":(-1, 0), "U":(0, -1), "D":(0, 1)}[d]
        x, y = x + dx*n, y + dy*n
        pts.append((x, y))
        perimeter += n
    
    shoelace = sum((a[0]*b[1]-b[0]*a[1]) for a,b in zip(pts, pts[1:]))//2
    return shoelace + perimeter//2 + 1

input_data = open("inputs/18.txt").readlines()

lines = [line.split() for line in input_data]
print("Part 1:", find_area(decode1(lines)))
print("Part 2:", find_area(decode2(lines)))