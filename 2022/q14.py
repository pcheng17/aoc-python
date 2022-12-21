from aocd import data
from copy import deepcopy

test = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


def parse(data):
    lines = data.splitlines()
    rocks = set()
    for line in lines:
        coordStrList = line.split(' -> ')
        coordList = [tuple(map(int, str.split(','))) for str in coordStrList]
        for c1, c2 in zip(coordList, coordList[1:]):
            x1, y1 = c1
            x2, y2 = c2
            rocks.update(
                (x, y)
                for x in range(min(x1, x2), max(x1, x2) + 1)
                for y in range(min(y1, y2), max(y1, y2) + 1)
            )
    return rocks


def isColliding(x, y, rocks, sand):
    return (x, y) in rocks or (x, y) in sand


def simulate(sand, rocks, yMax):
    def recursiveOp(x, y):
        if (x, y) in sand or (x, y) in rocks:
            return
        yield from recursiveOp(x, y + 1)
        yield from recursiveOp(x - 1, y + 1)
        yield from recursiveOp(x + 1, y + 1)
        sand.add((x, y))
        yield x, y

    yield from recursiveOp(500, 0)


def partA(rocks):
    yMax = max([y for _, y in rocks])
    sand = set()
    xCurr, yCurr = 500, 0
    while True:
        xCurr, yCurr = 500, 0
        while True:
            if yCurr >= yMax:
                return len(sand)
            if not isColliding(xCurr, yCurr+1, rocks, sand):
                yCurr += 1
            elif not isColliding(xCurr-1, yCurr+1, rocks, sand):
                xCurr -= 1
                yCurr += 1
            elif not isColliding(xCurr+1, yCurr+1, rocks, sand):
                xCurr += 1
                yCurr += 1
            else:
                sand.add((xCurr, yCurr))
                break


def partB(rocks):
    floorLevel = max([y for _, y in rocks]) + 2
    sand = set()
    xCurr, yCurr = 500, 0
    while True:
        xCurr, yCurr = 500, 0
        while True:
            if yCurr + 1 == floorLevel:
                sand.add((xCurr, yCurr))
                break
            elif not isColliding(xCurr, yCurr+1, rocks, sand):
                yCurr += 1
            elif not isColliding(xCurr-1, yCurr+1, rocks, sand):
                xCurr -= 1
                yCurr += 1
            elif not isColliding(xCurr+1, yCurr+1, rocks, sand):
                xCurr += 1
                yCurr += 1
            else:
                sand.add((xCurr, yCurr))
                if (500, 0) in sand:
                    return len(sand)
                break


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)

def myFun(x):
    print(x)

if __name__ == '__main__':
    rocks = parse(test)
    print(f'Part A: {partA(rocks)}')
    print(f'Part B: {partB(rocks)}')
