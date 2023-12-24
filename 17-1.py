import heapq

def a_star(grid):
    def heuristic(a, b):
        # Manhattan distance on a square grid
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def neighbors(node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for d in dirs:
            nx, ny = node[0] + d[0], node[1] + d[1]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                result.append((nx, ny))
        return result

    start, goal = (0, 0), (len(grid)-1, len(grid[0])-1)
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        # current_cost intentionally not used - used to retrieve the next most promising node, but not used afterwards
        current_cost, current = heapq.heappop(frontier)
        if current == goal:
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current] + grid[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # Add heurisstic to penalize paths that go further away from the end
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    # Reconstruct path
    current = goal
    path = []
    heat_loss = 0
    while current != start:
        path.append(current)
        heat_loss += grid[current[1]][current[0]]
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path, heat_loss


with open("inputs/17.txt") as f:
    grid = [[int(num) for num in row.strip()] for row in f.readlines()]

path, heat_loss = a_star(grid)
print(path)
print(heat_loss)
