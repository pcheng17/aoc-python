from aocd import data
from copy import deepcopy


test = '''
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
'''


RULES = {
    'N': [(-1, 0), (-1, -1), (-1, 1)],
    'S': [(1, 0), (1, -1), (1, 1)],
    'W': [(0, -1), (-1, -1), (1, -1)],
    'E': [(0, 1), (-1, 1), (1, 1)]
}

DIRS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def checkNorth(x, y, elves):
    scan = [(x + r[0], y + r[1]) for r in RULES['N']]
    if all(x not in elves for x in scan):
        return (x-1, y)
    else:
        return None

def checkSouth(x, y, elves):
    scan = [(x + r[0], y + r[1]) for r in RULES['S']]
    if all(x not in elves for x in scan):
        return (x+1, y)
    else:
        return None

def checkWest(x, y, elves):
    scan = [(x + r[0], y + r[1]) for r in RULES['W']]
    if all(x not in elves for x in scan):
        return (x, y-1)
    else:
        return None

def checkEast(x, y, elves):
    scan = [(x + r[0], y + r[1]) for r in RULES['E']]
    if all(x not in elves for x in scan):
        return (x, y+1)
    else:
        return None


def parse(data):
    elves = set() 
    elves.update(
        (i, j)
        for i, line in enumerate(data.strip().splitlines())
        for j, c in enumerate(line) if c == '#'
    )
    return elves


def partA(elves, rounds):
    ruleList = [checkNorth, checkSouth, checkWest, checkEast] 

    for _ in range(rounds):
        moves = {}
        noMove = set()
        for x, y in elves:
            nbrs = [(x + dir[0], y + dir[1]) for dir in DIRS]
            if all(x not in elves for x in nbrs):
                continue

            for rule in ruleList:
                result = rule(x, y, elves)
                if result is not None:
                    if result not in moves:
                        if result not in noMove:
                            moves[result] = (x, y)
                    else:
                        del moves[result]
                        noMove.add(result)
                    break
                    
        for dst, src in moves.items():
            elves.remove(src)
            elves.add(dst)

        ruleList = [ruleList[(i+1) % len(ruleList)] for i in range(len(ruleList))]


    xMin = min(x for x, _ in elves)
    xMax = max(x for x, _ in elves)
    yMin = min(y for _, y in elves)
    yMax = max(y for _, y in elves)

    return (yMax - yMin + 1) * (xMax - xMin + 1) - len(elves)

def partB(elves):
    ruleList = [checkNorth, checkSouth, checkWest, checkEast] 

    round = 0
    while True:
        round += 1
        moves = {}
        noMove = set()
        for x, y in elves:
            nbrs = [(x + dir[0], y + dir[1]) for dir in DIRS]
            if all(x not in elves for x in nbrs):
                continue

            for rule in ruleList:
                result = rule(x, y, elves)
                if result is not None:
                    if result not in moves:
                        if result not in noMove:
                            moves[result] = (x, y)
                    else:
                        del moves[result]
                        noMove.add(result)
                    break
                    
        if len(moves) == 0:
            return round

        for dst, src in moves.items():
            elves.remove(src)
            elves.add(dst)

        ruleList = [ruleList[(i+1) % len(ruleList)] for i in range(len(ruleList))]


def solveA(elves):
    return partA(deepcopy(elves), 10)


def solveB(elves):
    return partB(deepcopy(elves))


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
