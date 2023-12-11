def can_walk_north(c):
    return c == '|' or c == 'F' or c == '7'

def can_walk_east(c):
    return c == '-' or c == '7' or c == 'J'

def can_walk_south(c):
    return c == '|' or c == 'J' or c == 'L'

def can_walk_west(c):
    return c == '-' or c == 'L' or c == 'F'

def up(p):
    return (p[0]-1, p[1])

def down(p):
    return (p[0]+1, p[1])

def left(p):
    return (p[0], p[1]-1)

def right(p):
    return (p[0], p[1]+1)

def pretty_string(grid, pipe=None):
    mapping = {
        '-': '═',
        '|': '║',
        'F': '╔',
        '7': '╗',
        'J': '╝',
        'L': '╚',
        'S': '║',
        '.': '.'
    }
    res = [['.' for _ in grid[0]] for _ in grid]
    if pipe is None:
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                res[i][j] = mapping[col]
    else:
        for (x, y) in pipe:
            res[x][y] = mapping[grid[x][y]]
    return '\n'.join([''.join(row) for row in res])

def walk(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'S':
                x = i
                y = j
    sx = x
    sy = y

    a = []
    if can_walk_north(grid[x-1][y]):
        a.append((x-1, y))
    if can_walk_east(grid[x][y+1]):
        a.append((x, y+1))
    if can_walk_south(grid[x+1][y]):
        a.append((x+1, y))
    if can_walk_west(grid[x][y-1]):
        a.append((x, y-1))
    
    x = a[0][0]
    y = a[0][1]

    m = 1
    prev = (sx, sy)
    p = (x, y)

    pipes = set()
    pipes.add(prev)
    pipes.add(p)

    while grid[p[0]][p[1]] != 'S':
        match grid[p[0]][p[1]]:
            case '-':
                r = right(p)
                l = left(p) 
                nxt = r if r != prev else l
            case '|':
                u = up(p)
                d = down(p)
                nxt = u if u != prev else d
            case 'F':
                d = down(p)
                r = right(p)
                nxt = d if d != prev else r
            case '7':
                l = left(p)
                d = down(p)
                nxt = l if l != prev else d
            case 'J':
                l = left(p)
                u = up(p)
                nxt = l if l != prev else u
            case 'L':
                u = up(p)
                r = right(p)
                nxt = u if u != prev else r
            case _:
                print(f'Unknown char: {g[x][y]}')
        pipes.add(nxt)
        prev = p
        p = nxt
        m += 1
    
    return pipes

def part_a(input):
    grid = [[c for c in line] for line in input.splitlines()]
    pipes = walk(grid)
    return len(pipes) // 2

def part_b(input):
    grid = [[c for c in line] for line in input.splitlines()]

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'S':
                x = i
                y = j
    sx = x
    sy = y

    north = False
    east = False
    south = False
    west = False
    a = []
    if can_walk_north(grid[x-1][y]):
        north = True
        a.append((x-1, y))
    if can_walk_east(grid[x][y+1]):
        east = True
        a.append((x, y+1))
    if can_walk_south(grid[x+1][y]):
        south = True
        a.append((x+1, y))
    if can_walk_west(grid[x][y-1]):
        west = True
        a.append((x, y-1))
    
    x = a[0][0]
    y = a[0][1]

    m = 1
    prev = (sx, sy)
    p = (x, y)

    pipes = []
    pipes.append(prev)
    pipes.append(p)

    while grid[p[0]][p[1]] != 'S':
        match grid[p[0]][p[1]]:
            case '-':
                r = right(p)
                l = left(p) 
                nxt = r if r != prev else l
            case '|':
                u = up(p)
                d = down(p)
                nxt = u if u != prev else d
            case 'F':
                d = down(p)
                r = right(p)
                nxt = d if d != prev else r
            case '7':
                l = left(p)
                d = down(p)
                nxt = l if l != prev else d
            case 'J':
                l = left(p)
                u = up(p)
                nxt = l if l != prev else u
            case 'L':
                u = up(p)
                r = right(p)
                nxt = u if u != prev else r
            case _:
                print(f'Unknown char: {grid[x][y]}')
        pipes.append(nxt)
        prev = p
        p = nxt
        m += 1
    
    # str = pretty_string(grid, None)
    # with open('output.txt', 'w') as f:
    #     f.write(str)
    #     f.write('\n\n')
    #     for (x, y) in pipes:
    #         f.write(f'{x} {y}\n')

    t = [['.' for _ in grid[0]] for _ in grid]

    for (x, y) in pipes:
        if grid[x][y] == 'S':
            if north and east:
                t[x][y] = 'L'
            elif north and south:
                t[x][y] = '|'
            elif north and west:
                t[x][y] = 'J'
            elif east and south:
                t[x][y] = 'F'
            elif east and west:
                t[x][y] = '-'
            elif south and west:
                t[x][y] = '7'
        else:
            t[x][y] = grid[x][y]
        
    t = [
        ''.join(row)
        .replace('-', '')
        .replace('|', '1')
        .replace('FJ', '1')
        .replace('L7', '1')
        .replace('F7', '')
        .replace('LJ', '') for row in t
    ]


    inside = 0
    for row in t:
        count = 0
        for c in row:
            if c == '.':
                inside += count % 2
            else:
                count += int(c)
    return inside
