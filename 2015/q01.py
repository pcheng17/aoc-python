from aocd import data


def parse(data):
    return data.splitlines()


def partA(input):
    return sum(1 if c == '(' else -1 for c in input[0])


def partB(input):
    floor = 0
    for i, c in enumerate(input[0]):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i + 1


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
