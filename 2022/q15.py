from aocd import data
import time
import re

test = '''
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''

def parse(data):
    lines = data.split('\n')
    inputMap = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        sx, sy, bx, by = map(int, re.findall('-?[0-9]+', line))
        inputMap[(sx, sy)] = (bx, by)
    return inputMap


def manhattanDist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

def mergeIntervals(intervals):
    intervals = sorted(intervals, key = lambda x : x[0])

    result = []
    result.append(intervals[0])
    for x in intervals[1:]:
        if x[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][-1], x[1])
        else:
            result.append(x)

    return result

def mergeIntervalsB(intervals):
    intervals = sorted(intervals, key = lambda x : x[0])

    result = []
    smallestOverlap = None
    result.append(intervals[0])
    for x in intervals[1:]:
        if x[0] <= result[-1][1]:
            if smallestOverlap is None:
                smallestOverlap = result[-1][1] - x[0] + 1 
            else:
                smallestOverlap = min(smallestOverlap, result[-1][1] - x[0] + 1)
            result[-1][1] = max(result[-1][-1], x[1])
        else:
            result.append(x)

    return result, smallestOverlap


def partA(inputMap, y):
    distMap = {}
    for k, v in inputMap.items():
        distMap[k] = manhattanDist(k, v)

    intervals = []
    sensorCount = 0
    for k, v in distMap.items():
        vertDist = abs(k[1] - y)
        if vertDist == 0:
            sensorCount += 1
        if vertDist <= v:
            horizDist = v - vertDist
            leftEnd = k[0] - horizDist
            rightEnd = k[0] + horizDist
            if (leftEnd, y) in inputMap.values(): leftEnd += 1
            if (rightEnd, y) in inputMap.values(): rightEnd -= 1
            if rightEnd > leftEnd:
                intervals.append([leftEnd, 1 + rightEnd])
    
    intervals = mergeIntervals(intervals) 

    count = 0
    for r in intervals:
        count += r[1] - r[0]

    return count


def partB(inputMap):
    distMap = {}
    for k, v in inputMap.items():
        distMap[k] = manhattanDist(k, v)

    xMin = 0
    xMax = 4_000_000
    yMin = 0
    yMax = 4_000_000

    for y in range(yMin, yMax+1):
        tmp = []
        for k, v in distMap.items():
            vertDist = abs(k[1] - y)
            if vertDist <= v:
                horizDist = v - vertDist
                leftEnd = max(k[0] - horizDist, xMin)
                rightEnd = min(k[0] + horizDist, xMax)
                tmp.append([leftEnd, 1 + rightEnd])
        tmp = mergeIntervals(tmp)
        if len(tmp) != 1:
            yCoord = y 
            xCoord = tmp[0][1]
            return 4_000_000 * xCoord + yCoord


if __name__ == '__main__':
    inputMap = parse(data)

    start = time.time()
    print(f'Part A: {partA(inputMap, 2_000_000)}')
    end = time.time()
    print(f'{(end - start) * 1e6} microseconds')

    start = time.time()
    print(f'Part B: {partB(inputMap)}')
    end = time.time()
    print(f'{(end - start)} seconds')

