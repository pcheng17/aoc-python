import math
from heapq import heapify, heappush, heappop
from collections import defaultdict

def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dijkstra(grid, start):
    rows = len(grid)
    cols = len(grid[0])

    heat_loss = defaultdict(lambda: math.inf)

    # current heat loss, position, direction, same direction count
    queue = [
        (grid[0][1], (0, 1), '>', 1),
        (grid[1][0], (1, 0), 'v', 1),
    ]
    heapify(queue)

    while queue:
        hl, (i, j), d, sd = heappop(queue)

        if (i, j, d, sd) in heat_loss:
            continue

        heat_loss[(i, j, d, sd)] = min(heat_loss[(i, j, d, sd)], hl)

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
        else:
            if sd < 3 and in_bounds(grid, i + 1, j):
                heappush(queue, (hl + grid[i + 1][j], (i + 1, j), 'v', sd + 1))
            if in_bounds(grid, i, j + 1):
                heappush(queue, (hl + grid[i][j + 1], (i, j + 1), '>', 1))
            if in_bounds(grid, i, j - 1):
                heappush(queue, (hl + grid[i][j - 1], (i, j - 1), '<', 1))

    return min(hl for (i, j, _, _), hl in heat_loss.items() if i == rows - 1 and j == cols - 1)

def part_a(input):
    grid = [[int(c) for c in line] for line in input.splitlines()]
    return dijkstra(grid, (0, 0))

def part_b(input):
    grid = [[int(c) for c in line] for line in input.splitlines()]

    rows = len(grid)
    cols = len(grid[0])

    heat_loss = defaultdict(lambda: math.inf)

    # current heat loss, position, direction, same direction count
    queue = [
        (sum(grid[0][j] for j in range(1, 5)), (0, 4), '>', 4),
        (sum(grid[i][0] for i in range(1, 5)), (4, 0), 'v', 4),
    ]
    heapify(queue)

    while queue:
        hl, (i, j), d, sd = heappop(queue)

        if (i, j, d, sd) in heat_loss:
            continue

        heat_loss[(i, j, d, sd)] = min(heat_loss[(i, j, d, sd)], hl)

        if d == '>':
            if sd < 10 and in_bounds(grid, i, j + 1):
                heappush(queue, (hl + grid[i][j + 1], (i, j + 1), '>', sd + 1))
            if in_bounds(grid, i - 4, j):
                heappush(queue, (hl + sum(grid[i - k][j] for k in range(1, 5)), (i - 4, j), '^', 4))
            if in_bounds(grid, i + 4, j):
                heappush(queue, (hl + sum(grid[i + k][j] for k in range(1, 5)), (i + 4, j), 'v', 4))
        elif d == '^':
            if sd < 10 and in_bounds(grid, i - 1, j):
                heappush(queue, (hl + grid[i - 1][j], (i - 1, j), '^', sd + 1))
            if in_bounds(grid, i, j + 4):
                heappush(queue, (hl + sum(grid[i][j + k] for k in range(1, 5)), (i, j + 4), '>', 4))
            if in_bounds(grid, i, j - 4):
                heappush(queue, (hl + sum(grid[i][j - k] for k in range(1, 5)), (i, j - 4), '<', 4))
        elif d == '<':
            if sd < 10 and in_bounds(grid, i, j - 1):
                heappush(queue, (hl + grid[i][j - 1], (i, j - 1), '<', sd + 1))
            if in_bounds(grid, i - 4, j):
                heappush(queue, (hl + sum(grid[i - k][j] for k in range(1, 5)), (i - 4, j), '^', 4))
            if in_bounds(grid, i + 4, j):
                heappush(queue, (hl + sum(grid[i + k][j] for k in range(1, 5)), (i + 4, j), 'v', 4))
        else:
            if sd < 10 and in_bounds(grid, i + 1, j):
                heappush(queue, (hl + grid[i + 1][j], (i + 1, j), 'v', sd + 1))
            if in_bounds(grid, i, j + 4):
                heappush(queue, (hl + sum(grid[i][j + k] for k in range(1, 5)), (i, j + 4), '>', 4))
            if in_bounds(grid, i, j - 4):
                heappush(queue, (hl + sum(grid[i][j - k] for k in range(1, 5)), (i, j - 4), '<', 4))

    return min(hl for (i, j, _, _), hl in heat_loss.items() if i == rows - 1 and j == cols - 1)

# 662 -- too low

# 666 -- not right
# 669 -- not right

# 677 -- too high
# 694 -- too high
