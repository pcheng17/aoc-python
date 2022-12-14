from aocd import data
import copy
import numpy as np

test = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

def parse(data):
    lines = data.splitlines()
    allCoords = []
    for line in lines:
        coordStrList = line.split(' -> ')
        coordList = [np.array(list(map(int, str.split(','))), dtype=int) for str in coordStrList]
        allCoords.append(coordList)
    return allCoords

def simSand(grid, pos):
    # Down
    if grid[pos[1]+1][pos[0]] == '.':
        pos += np.array([1, 0], dtype=int)
        return simSand(grid, pos)
    else:


def partA(allCoords):
    # Find the bounding box for the walls
    minCoord = copy.deepcopy(allCoords[0][0])
    maxCoord = copy.deepcopy(allCoords[0][0])
    for coordList in allCoords:
        for coord in coordList:
            minCoord = np.minimum(minCoord, coord)
            maxCoord = np.maximum(maxCoord, coord)

    minCoord[1] = 0
    delta = copy.deepcopy(minCoord)

    sandStart = np.array([500, 0], dtype=int) - delta
    newMin = minCoord - delta
    newMax = maxCoord - delta
    nRows = newMax[0] - newMin[0] + 1
    nCols = newMax[1] - newMin[1] + 1

    #Create the grid
    grid = [['.' for _ in range(nRows)] for _ in range(nCols)]

    rocks = {}

    for coordList in allCoords:
        for idx in range(len(coordList)-1):
            start = coordList[idx]
            end = coordList[idx+1]
            segment = end - start
            if np.any(segment < 0):
                start, end = end, start
            for i in range(start[1], end[1]+1):
                for j in range(start[0], end[0]+1):
                    rocks[(i, j)] = 1

    grid[sandStart[1]][sandStart[0]] = '+'

    for row in grid:
        print(''.join(row))

    # Run simulation
    unitsOfSand = 0
    while True:
        sandPos = copy.deepcopy(sandStart)
        # down
        if grid[sandPos[1]+1][sandPos[0]] == '.'





            


def partB(input):
   raise NotImplementedError


if __name__ == '__main__':
    allCoords = parse(test)
    print(f'Part A: {partA(allCoords)}')
    # print(f'Part B: {partB(input)}')
