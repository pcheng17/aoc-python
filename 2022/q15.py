from aocd import data
from tqdm import tqdm
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

testSmall = '''
Sensor at x=8, y=7: closest beacon is at x=2, y=10
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
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def partA(inputMap):
    distMap = {}
    maxDist = -1
    for k, v in inputMap.items():
        distMap[k] = manhattanDist(k, v)
        if distMap[k] > maxDist:
            maxDist = distMap[k]

    lowerBound = list(inputMap.keys())[0][0]
    upperBound = list(inputMap.keys())[0][0]
    for s in inputMap.keys():
        lowerBound = min([lowerBound, s[0]])
        upperBound = max([upperBound, s[0]])
    lowerBound -= maxDist
    upperBound += maxDist
    
    count = 0
    visited = set()
    for i in tqdm(range(lowerBound, upperBound+1)):
        for k, v in distMap.items():
            pos = (i, 2000000)
            if pos not in inputMap.values() and pos not in inputMap.keys() and pos not in visited:
                if manhattanDist(pos, k) <= v:
                    count += 1
                    visited.add(pos)
    return count


def partB(input):
   raise NotImplementedError


if __name__ == '__main__':
    inputMap = parse(data)
    print(f'Part A: {partA(inputMap)}')
    # print(f'Part B: {partB(input)}')
