from collections import deque

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

possible_dirs = {
    'N': ['N', 'E', 'W'],
    'S': ['S', 'E', 'W'],
    'E': ['E', 'N', 'S'],
    'W': ['W', 'N', 'S']
}

def find_shortest_path(obstacles, start, start_dir, goal):
    visited = set()
    queue = deque([(start[0], start[1], start_dir, 0)])
    min_points = float('inf')

    while queue:
        x, y, curr_dir, points = queue.popleft()

        if (x, y) == goal:
            min_points = min(min_points, points)
            continue

        for next_dir in possible_dirs[curr_dir]:
            dx, dy = directions[next_dir]
            new_x, new_y = x + dx, y + dy

            new_points = points + (1000 if next_dir != curr_dir else 0) + 1

            state = (new_x, new_y, next_dir)
            if (new_x, new_y) in obstacles or new_points >= min_points:
                continue

            if state not in visited:
                visited.add(state)
                queue.append((new_x, new_y, next_dir, new_points))

    return min_points

def part_a(input):
    grid = [list(row) for row in input.splitlines()]
    obstacles = set()
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "#":
                obstacles.add((i, j))

    start = None
    goal = None
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                start = (i, j)
            if c == "E":
                goal = (i, j)

    return find_shortest_path(obstacles, start, 'E', goal)





def part_b(input):
    data = input.splitlines()
