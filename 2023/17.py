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
        i, j, d, sd, hl = heappop(queue)

        heat_loss = int(grid[i][j])

        # We've reached the end
        if i == rows - 1 and j == cols - 1:
            print(f'Found min heat loss: {hl + heat_loss}')
            min_heat_loss = min(min_heat_loss, hl + heat_loss)
            continue


        # if (i, j) in visited and min_heat_loss < visited[(i, j)]:
        #     continue

        # visited[(i, j, d, sd)] = hl

        if d == '>':
            if sd < 3:
                tmp.append((i, j + 1, '>', sd + 1, hl + heat_loss))
            tmp.append((i + 1, j, 'V', 0, hl + heat_loss))
            tmp.append((i - 1, j, '^', 0, hl + heat_loss))
        elif dir == '^':
            if sd < 3:
                tmp.append((i - 1, j, '^', sd + 1, hl + heat_loss))
            tmp.append((i, j - 1, '<', 0, hl + heat_loss))
            tmp.append((i, j + 1, '>', 0, hl + heat_loss))
        elif dir == '<':
            if sd < 3:
                tmp.append((i, j - 1, '<', sd + 1, hl + heat_loss))
            tmp.append((i + 1, j, 'V', 0, hl + heat_loss))
            tmp.append((i - 1, j, '^', 0, hl + heat_loss))
        else: # dir == 'V'
            if sd < 3:
                tmp.append((i + 1, j, 'V', sd + 1, hl + heat_loss))
            tmp.append((i, j - 1, '<', 0, hl + heat_loss))
            tmp.append((i, j + 1, '>', 0, hl + heat_loss))

def part_a(input):
    data = tuple(input.splitlines())
    # (i, j, dir, same_dir_count, heat_loss)
    queue = [
        (0, 0, '>', 0, -int(data[0][0])),
        (0, 0, 'V', 0, -int(data[0][0]))
    ]
    heapify(queue)
    return solve(data, queue)

def part_b(input):
    data = input.splitlines()
