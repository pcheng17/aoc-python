from aocd import data
from itertools import zip_longest
from tqdm import tqdm


test ='''
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''

# First elements of each list is the bottom row!
ROCKS = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0011100, 0b0000100, 0b0000100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000]
]


def parse(data):
    return [c for c in data.strip()]


def singleStep(tower, rock, wind):
    if wind == '>':
        if not any(line & 0b0000001 for line in rock) and not any(
                (r >> 1) & t for r, t in zip(rock, tower)):
            rock = [line >> 1 for line in rock]
    else:
        if not any(line & 0b1000000 for line in rock) and not any(
                (r << 1) & t for r, t in zip(rock, tower)):
            rock = [line << 1 for line in rock]

    if any((r & t) for r, t in zip_longest(rock[1:], tower, fillvalue=0)):
        return (rock, True)
    else:
        return (rock[1:], False)


def sim(winds, numRocks):
    tower = [0b1111111]

    wIdx = 0

    heights = [0]
    for i in tqdm(range(numRocks)):
        rock = [0] * len(tower) + [0, 0, 0] + ROCKS[i % len(ROCKS)]
        stopped = False
        while not stopped:
            rock, stopped = singleStep(tower, rock, winds[wIdx])
            wIdx = (wIdx + 1) % len(winds)
        new_tower = [(r | t) for r, t in zip_longest(rock, tower, fillvalue=0)] 
        heights.append(len(new_tower)-1)
        tower = new_tower

    return tower, heights


def partA(input, numRocks):
    tower, _ = sim(input, numRocks)
    return len(tower) - 1


def partB(input):
    tower, heights = sim(input, 5000)
    print(heights.index(1141)) # Height of when periodicity begins
    print(heights.index(3878)) # Height of when periodicity ends

    # Printing the index tells me at what rock indices periodicity begins and ends

    # I realized that there are 1369 rocks left at the end of the simulation
    # that don't get included included in the periodicity, so I need to figure
    # out how much height those last 1369 will add
    print(heights[711 + 1369] - heights[711])

    return len(tower) - 1


def solveA(input):
    return partA(input, 2022)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
