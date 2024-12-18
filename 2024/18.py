from collections import deque

def find_shortest_path(sz, obstacles, start, goal):
    def is_valid(x, y):
        return (0 <= x < sz and 0 <= y < sz and (x, y) not in obstacles)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = {start}
    queue = deque([(start[0], start[1], [start])])

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == goal:
            return path

        # Try all four directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)

            if is_valid(new_x, new_y) and new_pos not in visited:
                visited.add(new_pos)
                new_path = path + [new_pos]
                queue.append((new_x, new_y, new_path))

    return None

def part_a(input):
    data = input.splitlines()
    n = 1024
    sz = 71
    byte_pos = []
    for row in data:
        a, b = map(int, row.split(","))
        byte_pos.append((a, b))

    obstacles = set()
    for i in range(n):
        obstacles.add(byte_pos[i])

    start = (0, 0)
    goal = (sz - 1, sz - 1)

    path = find_shortest_path(sz, obstacles, start, goal)
    if path:
        return len(path) - 1

def part_b(input):
    data = input.splitlines()
    sz = 71
    byte_pos = []
    for row in data:
        a, b = map(int, row.split(","))
        byte_pos.append((a, b))

    start = (0, 0)
    goal = (sz - 1, sz - 1)

    a = 0
    b = len(byte_pos)

    while b - a > 1:
        mid = (a + b) // 2
        obstacles = set()
        for i in range(mid):
            obstacles.add(byte_pos[i])
        if find_shortest_path(sz, obstacles, start, goal) is None:
            b = mid
        else:
            a = mid
    return f"{byte_pos[a][0]},{byte_pos[a][1]}"

