from aocd import data
from copy import deepcopy

test = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


DIRS = [
    (-1, -1),
    (1, -1)
]

def parse(data):
    lines = data.splitlines()
    allCoords = []
    for line in lines:
        coordStrList = line.split(' -> ')
        coordList = [tuple(map(int, str.split(','))) for str in coordStrList]
        allCoords.append(coordList)
    return allCoords

# def simSand(grid, pos):
#     # Down
#     if grid[pos[1]+1][pos[0]] == '.':
#         pos += np.array([1, 0], dtype=int)
#         return simSand(grid, pos)
#     else:


def partA(input):
    rocks = set()

    for row in input:
        for idx in range(len(row)-1):
            start = row[idx]
            end = row[idx+1]
            if end[0] < start[0] or end[1] < start[1]:
                start, end = end, start
            for i in range(start[0], end[0]+1):
                for j in range(start[1], end[1]+1):
                    rocks.add((i, j))
    




                





    # # Run simulation
    # unitsOfSand = 0
    # while True:
    #     sandPos = copy.deepcopy(sandStart)
    #     # down
    #     if grid[sandPos[1]+1][sandPos[0]] == '.'


def partB(input):
    pass


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    allCoords = parse(test)
    print(f'Part A: {partA(allCoords)}')
    # print(f'Part B: {partB(input)}')
