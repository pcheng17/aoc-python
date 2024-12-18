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
    visited = {(start[0], start[1], start_dir): 0}
    queue = deque([(start[0], start[1], start_dir, 0)])
    min_points = float('inf')

    while queue:
        x, y, curr_dir, points = queue.popleft()

        if (x, y) == goal:
            min_points = min(min_points, points)
            continue

        for next_dir in possible_dirs[curr_dir]:
            if next_dir == curr_dir:
                # Step
                dx, dy = directions[curr_dir]
                new_x, new_y = x + dx, y + dy
                new_points = points + 1
                state = (new_x, new_y, curr_dir)
                if (new_x, new_y) in obstacles or new_points > min_points:
                    continue
                if state not in visited or new_points < visited[state]:
                    visited[state] = new_points
                    queue.append((new_x, new_y, curr_dir, new_points))
            else:
                # Turn
                new_points = points + 1000
                state = (x, y, next_dir)
                if new_points > min_points:
                    continue
                if state not in visited or new_points < visited[state]:
                    visited[state] = new_points
                    queue.append((x, y, next_dir, new_points))

    return min_points

def find_all_tiles_of_best_paths(obstacles, start, start_dir, goal, goal_points):
    visited = {(start[0], start[1], start_dir, (start,)): 0}
    queue = deque([(start[0], start[1], start_dir, (start,), 0)])

    all_tiles = set()
    while queue:
        x, y, curr_dir, path, points = queue.popleft()

        if (x, y) == goal:
            if points == goal_points:
                for tile in path:
                    all_tiles.add(tile)
            continue

        for next_dir in possible_dirs[curr_dir]:
            if next_dir == curr_dir:
                # Step
                dx, dy = directions[curr_dir]
                new_x, new_y = x + dx, y + dy
                new_points = points + 1
                if (new_x, new_y) in obstacles or new_points > goal_points:
                    continue
                new_path = (*path, (new_x, new_y))
                state = (new_x, new_y, curr_dir, new_path)
                if state not in visited or new_points < visited[state]:
                    visited[state] = new_points
                    queue.append((new_x, new_y, curr_dir, new_path, new_points))
            else:
                # Turn
                new_points = points + 1000
                if new_points > goal_points:
                    continue
                state = (x, y, next_dir, path)
                if state not in visited or new_points < visited[state]:
                    visited[state] = new_points
                    queue.append((x, y, next_dir, path, new_points))

    return all_tiles

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

    return len(find_all_tiles_of_best_paths(obstacles, start, 'E', goal, 92432))
