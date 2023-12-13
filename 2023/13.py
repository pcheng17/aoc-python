def levenshtein(a, b):
    return sum(int(x != y) for x, y in zip(a, b))

def scan(grid, s):
    '''Scan for a horizontal reflection in the grid, allowing for `s` many smudges'''
    for i in range(len(grid)-1):
        if sum(levenshtein(r1, r2) for r1, r2 in zip(grid[i::-1], grid[i+1:])) == s:
            return i+1
    return 0

def part_a(input):
    grids = [group.split() for group in input.split('\n\n')]
    # Vertical reflection + 100 * horizontal reflection
    return sum(scan([*zip(*g)], 0) + 100 * scan(g, 0) for g in grids)

def part_b(input):
    grids = [group.split() for group in input.split('\n\n')]
    # Vertical reflection + 100 * horizontal reflection
    return sum(scan([*zip(*g)], 1) + 100 * scan(g, 1) for g in grids)
