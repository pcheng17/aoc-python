from collections import deque, defaultdict
from common.utils import manhattan
import numpy as np

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_path(walkway, start, goal):
    path = [start]
    visited = set()
    visited.add(start)
    curr = start
    while curr != goal:
        for d in directions:
            next = (curr[0] + d[0], curr[1] + d[1])
            if next in walkway and next not in visited:
                path.append(next)
                visited.add(next)
                curr = next
                break
    return path

def bfs(walkway, start, goal):
    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])
    while queue:
        curr, time = queue.popleft()
        if curr == goal:
            return time
        for d in directions:
            next = (curr[0] + d[0], curr[1] + d[1])
            if next in walkway and next not in visited:
                queue.append((next, time + 1))
                visited.add(next)
    return -1

def part_a(input):
    data = input.splitlines()
    walkway = set()
    start = None
    goal = None
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == ".":
                walkway.add((i, j))
            if c == "S":
                start = (i, j)
            if c == "E":
                goal = (i, j)
                walkway.add((i, j))

    path = get_path(walkway, start, goal)
    total_time = len(path) - 1

    cheat_times = []
    for i, tile in enumerate(path):
        for dx, dy in directions:
            skipover = (tile[0] + dx, tile[1] + dy)
            skipto = (tile[0] + dx + dx, tile[1] + dy + dy)
            if skipover not in walkway and skipto in path:
                j = path.index(skipto)
                if j > i:
                    cheat_times.append(total_time - (j - i) + 2)

    return sum([1 for t in cheat_times if total_time - t >= 100])

def part_b(input):
    data = input.splitlines()
    walkway = set()
    obstacles = set()
    start = None
    goal = None
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == ".":
                walkway.add((i, j))
            if c == "S":
                start = (i, j)
            if c == "E":
                goal = (i, j)
                walkway.add((i, j))
            if c == "#":
                obstacles.add((i, j))

    path = get_path(walkway, start, goal)
    xs = np.array([x for x, _ in path])
    ys = np.array([y for _, y in path])

    n = len(xs)
    i, j = np.triu_indices(n, k=100)

    dx = np.abs(xs[i] - xs[j])
    dy = np.abs(ys[i] - ys[j])
    distances = dx + dy
    saved_time = (j - i) - distances

    return np.sum((distances <= 20) & (saved_time >= 100))

