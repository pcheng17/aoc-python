def levenshtein(a, b):
    d = sum(int(x != y) for x, y in zip(a, b))
    return d + abs(len(a) - len(b))

def scan_vertical_a(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    for j in range(cols-1):
        mirror = True
        for a, b in zip(range(j, -1, -1), range(j+1, cols)):
            col1 = [grid[i][a] for i in range(rows)]
            col2 = [grid[i][b] for i in range(rows)]
            if col1 == col2:
                continue
            else:
                mirror = False
                break
        if mirror:
            return j+1
    return 0

def scan_horizontal_a(grid):
    rows = len(grid)

    for i in range(rows-1):
        mirror = True
        for a, b in zip(range(i, -1, -1), range(i+1, rows)):
            if grid[a] == grid[b]:
                continue
            else:
                mirror = False
                break
        if mirror:
            return i+1
    return 0

def scan_vertical_b(grid):
    rows = len(grid)
    cols = len(grid[0])
 
    for j in range(cols-1):
        mirror = True
        lev = 0
        for a, b in zip(range(j, -1, -1), range(j+1, cols)):
            col1 = [grid[i][a] for i in range(rows)]
            col2 = [grid[i][b] for i in range(rows)]
            if col1 != col2:
                lev += levenshtein(col1, col2)
        if lev == 1:
            return j + 1
    return 0

def scan_horizontal_b(grid):
    rows = len(grid)

    for i in range(rows-1):
        mirror = True
        lev = 0
        for a, b in zip(range(i, -1, -1), range(i+1, rows)):
            if grid[a] != grid[b]:
                lev += levenshtein(grid[a], grid[b])
        if lev == 1:
            return i+1
    return 0

def part_a(input):
    grids = [group.split() for group in input.split('\n\n')]
    return sum(scan_vertical_a(g) + 100 * scan_horizontal_a(g) for g in grids)

def part_b(input):
    grids = [group.split() for group in input.split('\n\n')]
    return sum(scan_vertical_b(g) + 100 * scan_horizontal_b(g) for g in grids)
