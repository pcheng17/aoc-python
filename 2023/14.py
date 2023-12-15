def t(grid):
    '''Tranpose the grid of strings into a new grid of strings'''
    return list(map(''.join, zip(*grid)))

def s(grid, s):
    '''Slide rocks...magically'''
    for i in range(len(grid)):
        for _ in range(len(grid[i])):
            tmp = grid[i].replace(*s.split('|'))
            if tmp != grid[i]:
                grid[i] = tmp
            else:
                break
    return grid

def sw(grid):
    '''Slide rocks to the west'''
    return s(grid, '.O|O.')

def se(grid):
    '''Slide rocks to the east'''
    return s(grid, 'O.|.O')

def score(grid):
    return sum((len(grid) - i) * (c == 'O') for i, row in enumerate(grid) for c in row)

def part_a(input):
    return score(t(sw(t(input.splitlines()))))

def part_b(input):
    cycles = 1000000000
    grid = input.splitlines()
    cycle = lambda grid: se(t(se(t(sw(t(sw(t(grid))))))))

    history = {''.join(grid): (0, score(grid))}
    for idx in range(1, cycles + 1):
        grid = cycle(grid)
        k = ''.join(grid)
        if k in history:
            period = idx - history[k][0]
            break
        else:
            history[k] = (idx, score(grid))

    for i, s in [v for v in history.values() if history[k][0] <= v[0] <= idx]:
        if i % period == cycles % period:
            return s
