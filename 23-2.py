# By u/qwewqa
with open("inputs/23.txt") as f:
    data = f.read().strip().splitlines()

edges = {}  # (r, c) -> (ar, ac, length)
for r, row in enumerate(data):
    for c, tile in enumerate(row):
        if tile in ".>v": # not all possible slopes are used
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ar, ac = r + dr, c + dc
                if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                    continue
                if data[ar][ac] in ".>v":
                    edges.setdefault((r, c), set()).add((ar, ac, 1))
                    edges.setdefault((ar, ac), set()).add((r, c, 1))

while True:
    for n, e in edges.items():
        if len(e) == 2:
            # Where n has two neighbors a,b -> remove n and make a and b neighbors instead
            a, b = e
            edges[a[:2]].remove(n + (a[2],))
            edges[b[:2]].remove(n + (b[2],))
            edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
            edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
            del edges[n]
            break
    else:
        break

row_len, col_len = len(data), len(data[0])

start_pos = (0, 1, 0)
end_pos = (row_len - 1, col_len - 2)
queue = [start_pos]
visisted = set()
best = 0
while queue:
    r, c, d = queue.pop()
    if d == -1:
        visisted.remove((r, c))
        continue
    if (r, c) == end_pos:
        best = max(best, d)
        continue
    if (r, c) in visisted:
        continue
    visisted.add((r, c))
    queue.append((r, c, -1))
    for ar, ac, l in edges[(r, c)]:
        queue.append((ar, ac, d + l))

print(best)