import math
from heapq import heapify, heappush, heappop
from collections import defaultdict

def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dijkstra(grid, start):
    rows = len(grid)
    cols = len(grid[0])

    visited = {start}
    heat_loss = defaultdict(lambda: math.inf)
    heat_loss[start] = 0

    # current heat loss, position, direction, same direction count
    queue = [
        (int(grid[0][1]), (0, 1), '>', 1),
        (int(grid[1][0]), (1, 0), 'v', 1),
    ]
    heapify(queue)

    while queue:
        hl, (i, j), d, sd = heappop(queue)
        print(f'{hl} {i} {j} {d} {sd}')

        if (i, j, d) in visited:
            continue

        visited.add((i, j, d))
        heat_loss[(i, j)] = min(heat_loss[(i, j)], hl)

        if d == '>':
            if sd < 3 and in_bounds(grid, i, j + 1):
                heappush(queue, (hl + grid[i][j + 1], (i, j + 1), '>', sd + 1))
            if in_bounds(grid, i - 1, j):
                heappush(queue, (hl + grid[i - 1][j], (i - 1, j), '^', 1))
            if in_bounds(grid, i + 1, j):
                heappush(queue, (hl + grid[i + 1][j], (i + 1, j), 'v', 1))
        elif d == '^':
            if sd < 3 and in_bounds(grid, i - 1, j):
                heappush(queue, (hl + grid[i - 1][j], (i - 1, j), '^', sd + 1))
            if in_bounds(grid, i, j + 1):
                heappush(queue, (hl + grid[i][j + 1], (i, j + 1), '>', 1))
            if in_bounds(grid, i, j - 1):
                heappush(queue, (hl + grid[i][j - 1], (i, j - 1), '<', 1))
        elif d == '<':
            if sd < 3 and in_bounds(grid, i, j - 1):
                heappush(queue, (hl + grid[i][j - 1], (i, j - 1), '<', sd + 1))
            if in_bounds(grid, i - 1, j):
                heappush(queue, (hl + grid[i - 1][j], (i - 1, j), '^', 1))
            if in_bounds(grid, i + 1, j):
                heappush(queue, (hl + grid[i + 1][j], (i + 1, j), 'v', 1))
        elif d == 'v':
            if sd < 3 and in_bounds(grid, i + 1, j):
                heappush(queue, (hl + grid[i + 1][j], (i + 1, j), 'v', sd + 1))
            if in_bounds(grid, i, j + 1):
                heappush(queue, (hl + grid[i][j + 1], (i, j + 1), '>', 1))
            if in_bounds(grid, i, j - 1):
                heappush(queue, (hl + grid[i][j - 1], (i, j - 1), '<', 1))

    return heat_loss[(rows - 1, cols - 1)]

def part_a(input):
    grid = [[int(c) for c in line] for line in input.splitlines()]
    return dijkstra(grid, (0, 0))

def part_b(input):
    data = input.splitlines()

# 662 -- too low

# 669 not right
# 677 -- too high
# 694 -- too high
