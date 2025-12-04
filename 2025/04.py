def build_grid(data):
    grid = []
    rows = len(data)
    cols = len(data[0])

    grid = [['.' for _ in range(cols + 2)]]
    for row in data:
        tmp = ['.']
        tmp.extend([c for c in row])
        tmp.append('.')
        grid.append(tmp)
    grid.append(['.' for _ in range(cols + 2)])
    return grid, rows, cols

def count_neighbors(grid, r, c):
    count = 0
    if grid[r - 1][c] == '@':
        count += 1
    if grid[r + 1][c] == '@':
        count += 1
    if grid[r][c - 1] == '@':
        count += 1
    if grid[r][c + 1] == '@':
        count += 1
    if grid[r-1][c-1] == '@':
        count += 1
    if grid[r-1][c+1] == '@':
        count += 1
    if grid[r+1][c-1] == '@':
        count += 1
    if grid[r+1][c+1] == '@':
        count += 1
    return count

def part_a(input):
    data = input.splitlines()
    grid, rows, cols = build_grid(data)
    ans = 0

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if grid[r][c] == '@':
                if count_neighbors(grid, r, c) < 4:
                    ans += 1
    return ans


def part_b(input):
    data = input.splitlines()
    grid, rows, cols = build_grid(data)
    ans = 0

    while True:
        removed_any = False
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if grid[r][c] == '@':
                    if count_neighbors(grid, r, c) < 4:
                        grid[r][c] = '.'
                        ans += 1
                        removed_any = True
        if not removed_any:
            break
    return ans
