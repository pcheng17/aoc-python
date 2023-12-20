import math

def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def solve(grid, frontier):
    rows = len(grid)
    cols = len(grid[0])

    min_heat_loss = math.inf

    visited = set()

    while True:
        next_frontier = []
        for i, j, d, sd, hl in frontier:
            heat_loss = int(grid[i][j])

            # We've reached the end
            if i == rows - 1 and j == cols - 1:
                print(f'Found min heat loss: {hl + heat_loss}')
                min_heat_loss = min(min_heat_loss, hl + heat_loss)
                continue

            # We've already visited this state
            if (i, j, d) in visited:
                continue

            visited.add((i, j, d))
            tmp = []
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

            tmp = [x for x in tmp if in_bounds(grid, x[0], x[1])]
            print(f'({i}, {j}, {d}, {sd}, {hl}) -> {tmp}')
            next_frontier.extend(tmp)
        next_frontier = [x for x in next_frontier if x[4] < min_heat_loss]
        next_frontier = [x for x in next_frontier if in_bounds(grid, x[0], x[1])]
        if not next_frontier:
            return min_heat_loss
        else:
            frontier = next_frontier

def part_a(input):
    data = tuple(input.splitlines())
    frontier = [(0, 0, '>', 0, -int(data[0][0]))] # (i, j, dir, same_dir_count, heat_loss)
    return solve(data, frontier)

def part_b(input):
    data = input.splitlines()
