""" LCM solution by u/leijurv """

ll = [x for x in open("day-8-data.txt").read().strip().split('\n\n')]
import math
inst = list(ll[0])
conn = {}
for l in ll[1].split("\n"):
	a = l.split(" ")[0]
	b = l.split("(")[1].split(",")[0]
	c = l.split(" ")[3].split(")")[0]
	conn[a] = (b, c)
pos = 'AAA'
idx = 0
while pos != 'ZZZ':
	d = inst[idx%len(inst)]
	pos = conn[pos][0 if d=='L' else 1]
	idx += 1
print("p1", idx)
def solvesteps(start):
	pos = start
	idx = 0
	while not pos.endswith('Z'):
		d = inst[idx%len(inst)]
		pos = conn[pos][0 if d=='L' else 1]
		idx += 1
	return idx
ret = 1
for start in conn:
	if start.endswith('A'):
		ret = math.lcm(ret, solvesteps(start))
print("p2", ret)

""" My brute force solution - takes way too long """
"""
with open ("day-8-data.txt") as f:
    data_raw = f.readlines()
    data_raw = [row.strip() for row in data_raw]

    instructions = data_raw[0]    
    nodes = {}
    for row in data_raw[2:]:
        elements = row.split()
        node_name = elements[0]
        left = elements[2][1:-1]
        right = elements[3][:-1]
        nodes[node_name] = [left, right]

instruction_map = {
    "L":0,
    "R":1
}

current_nodes = ["AAA", "PRA", "PVA", "XLA", "PTA", "FBA"]
step_count = 0

# Loop instructions
for _ in range(100000000):
    print(_)
    for char in instructions:
        for i, node in enumerate(current_nodes):
            current_nodes[i] = nodes[node][instruction_map[char]]

        step_count +=1


        if all([node[2] == "Z" for node in current_nodes]):
            print(step_count)
            quit()
"""