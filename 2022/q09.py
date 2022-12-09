from aocd import data
import numpy as np

e1 = np.array([1, 0], dtype=int)
e2 = np.array([0, 1], dtype=int)
origin = np.array([0, 0], dtype=int)

DIR = {
    'U': e2,
    'D': -e2,
    'L': -e1,
    'R': e1
}

test = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'
]

testB = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]


def parse(data):
    return data.splitlines()


def findMove(dp):
    absdp = np.abs(dp)
    maxValue = np.max(absdp)
    whereMax = absdp == maxValue
    dp -= np.multiply(np.sign(dp), whereMax)
    return dp


def partA(moves):
    hPos = np.copy(origin)
    tPos = np.copy(origin)

    locs = set()
    locs.add(tuple(tPos))

    for move in moves:
        d, s = move.split()
        for _ in range(int(s)):
            hPos += DIR[d]
            dp = hPos - tPos
            tPos += findMove(dp);
            locs.add(tuple(tPos))
    return len(locs)


def partB(moves):
    hPos = np.copy(origin)
    knots = [np.copy(origin) for _ in range(9)]

    locs = set()
    locs.add(tuple(np.copy(origin)))

    for move in moves:
        d, s = move.split()
        for _ in range(int(s)):
            hPos += DIR[d]
            ahead = hPos
            for knot in knots:
                dp = ahead - knot
                knot += findMove(dp)
                ahead = knot
            locs.add(tuple(knots[-1]))
    return len(locs)


moves = parse(data)
print(f'Part A: {partA(moves)}')
print(f'Part B: {partB(moves)}')
