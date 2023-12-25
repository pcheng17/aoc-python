import math
from heapq import heapify, heappush, heappop

def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve(grid, queue):
    rows = len(grid)
    cols = len(grid[0])

    min_heat_loss = math.inf

    visited = {}

    while queue:
        hl, (i, j), d, sd, visited = heappop(queue)

        if not in_bounds(grid, i, j):
            continue

        if (i, j) in visited:
            continue

        visited.add((i, j))

        heat_loss = int(grid[i][j])

        if i == rows - 1 and j == cols - 1:
            print(f'Found min heat loss: {hl + heat_loss}')
            print(f'Visited: {visited}')
            min_heat_loss = min(min_heat_loss, hl + heat_loss)
            continue

        if hl + heat_loss >= min_heat_loss:
            continue

        if d == '>':
            if sd < 3:
                heappush(queue, (hl + heat_loss, (i, j + 1), '>', sd + 1, visited.copy()))
            heappush(queue, (hl + heat_loss, (i - 1, j), '^', 0, visited.copy()))
            heappush(queue, (hl + heat_loss, (i + 1, j), 'v', 0, visited.copy()))
        elif dir == '^':
            if sd < 3:
                heappush(queue, (hl + heat_loss, (i - 1, j), '^', sd + 1, visited.copy()))
            heappush(queue, (hl + heat_loss, (i, j + 1), '>', 0, visited.copy()))
            heappush(queue, (hl + heat_loss, (i, j - 1), '<', 0, visited.copy()))
        elif dir == '<':
            if sd < 3:
                heappush(queue, (hl + heat_loss, (i, j - 1), '<', sd + 1, visited.copy()))
            heappush(queue, (hl + heat_loss, (i - 1, j), '^', 0, visited.copy()))
            heappush(queue, (hl + heat_loss, (i + 1, j), 'v', 0, visited.copy()))
        else: # dir == 'v'
            if sd < 3:
                heappush(queue, (hl + heat_loss, (i + 1, j), 'v', sd + 1, visited.copy()))
            heappush(queue, (hl + heat_loss, (i, j + 1), '>', 0, visited.copy()))
            heappush(queue, (hl + heat_loss, (i, j - 1), '<', 0, visited.copy()))

    return min_heat_loss

def part_a(input):
    data = tuple(input.splitlines())
    # (heat_loss, (i, j), dir, same_dir_count)
    queue = [
        (-int(data[0][0]), (0, 0), '>', -1, set()),
    ]
    heapify(queue)
    return solve(data, queue)

def part_b(input):
    data = input.splitlines()
