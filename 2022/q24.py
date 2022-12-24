from aocd import data
from copy import deepcopy


test = '''
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
'''

DIRS = ['^', 'v', '>', '<']

NBRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def parse(data):
    walls = set()
    north, south, east, west = set(), set(), set(), set()
    for i, line in enumerate(data.strip().splitlines()):
        for j, c in enumerate(line):
            match c:
                case '#': walls.add((i, j))
                case '^': north.add((i, j))
                case 'v': south.add((i, j))
                case '>': east.add((i, j))
                case '<': west.add((i, j))

    return walls, north, south, east, west


def advanceBlizzard(walls, north, south, east, west):
    nRows = max([i for i, _ in walls]) + 1
    nCols = max([j for _, j in walls]) + 1
    northp1, southp1, eastp1, westp1 = set(), set(), set(), set()
    northp1.update((x-1 if x-1 != 0 else nRows - 2, y) for x, y in north)
    southp1.update((x+1 if x+1 != nRows - 1 else 1, y) for x, y in south)
    eastp1.update((x, y+1 if y+1 != nCols - 1 else 1) for x, y in east)
    westp1.update((x, y-1 if y-1 != 0 else nCols - 2) for x, y in west)
    return northp1, southp1, eastp1, westp1


def draw(walls, north, south, east, west):
    nRows = max([i for i, _ in walls]) + 1
    nCols = max([j for _, j in walls]) + 1

    grid = [['.' for _ in range(nCols)] for _ in range(nRows)]

    for i, j in walls: grid[i][j] = '#'
    for i, j in north: 
        if grid[i][j] in DIRS:
            grid[i][j] = '2'
        elif grid[i][j].isnumeric():
            grid[i][j] = str(int(grid[i][j]) + 1)
        else:
            grid[i][j] = '^'
    for i, j in south: 
        if grid[i][j] in DIRS:
            grid[i][j] = '2'
        elif grid[i][j].isnumeric():
            grid[i][j] = str(int(grid[i][j]) + 1)
        else:
            grid[i][j] = 'v'
    for i, j in east: 
        if grid[i][j] in DIRS:
            grid[i][j] = '2'
        elif grid[i][j].isnumeric():
            grid[i][j] = str(int(grid[i][j]) + 1)
        else:
            grid[i][j] = '>'
    for i, j in west: 
        if grid[i][j] in DIRS:
            grid[i][j] = '2'
        elif grid[i][j].isnumeric():
            grid[i][j] = str(int(grid[i][j]) + 1)
        else:
            grid[i][j] = '<'

    for row in grid:
        print(''.join(row))


def inBounds(pos, walls, start, end):
    nRows = max([i for i, _ in walls]) + 1
    nCols = max([j for _, j in walls]) + 1
    if pos[0] >= 1 and pos[1] >= 1 and pos[0] < nRows-1 and pos[1] < nCols-1:
        return True
    elif pos == start or pos == end:
        return True


def simulate(walls, north, south, east, west, start, end):
    frontier = set()
    frontier.add(start)

    count = 0

    while frontier:
        for x, y in frontier:
            if x == end[0] and y == end[1]:
                return count, north, south, east, west

        north, south, east, west = advanceBlizzard(walls, north, south, east, west)
        tmp = set()
        for x, y in frontier:
            nbrs = [(x + n[0], y + n[1]) for n in NBRS]
            for nbr in nbrs:
                if inBounds(nbr, walls, start, end):
                    checks = [nbr not in x for x in [north, south, east, west]]
                    if all(checks):
                        tmp.add(nbr)

            checks = [(x, y) not in b for b in [north, south, east, west]]
            if all(checks):
                tmp.add((x, y))

        frontier = tmp
        count += 1

    return count, north, south, east, west


def partA(walls, north, south, east, west, start, end):
    trip, *_ = simulate(walls, north, south, east, west, start, end)
    return trip


def partB(walls, north, south, east, west, start, end):
    trip1, north, south, east, west = simulate(walls, north, south, east, west, start, end)
    trip2, north, south, east, west = simulate(walls, north, south, east, west, end, start)
    trip3, north, south, east, west = simulate(walls, north, south, east, west, start, end)
    return trip1 + trip2 + trip3


def solveA(input):
    walls, north, south, east, west = input
    nRows = max([i for i, _ in walls]) + 1
    nCols = max([j for _, j in walls]) + 1
    start = (0, 1)
    end = (nRows - 1, nCols -2)
    return partA(walls, deepcopy(north), deepcopy(south), deepcopy(east), deepcopy(west), start, end)


def solveB(input):
    walls, north, south, east, west = input
    nRows = max([i for i, _ in walls]) + 1
    nCols = max([j for _, j in walls]) + 1
    start = (0, 1)
    end = (nRows - 1, nCols -2)
    return partB(walls, deepcopy(north), deepcopy(south), deepcopy(east), deepcopy(west), start, end)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
