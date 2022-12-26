from aocd import data


def parse(data):
    return list(map(int, data.splitlines()))


def partA(input):
    return sum([b > a for a, b in zip(input, input[1:])])


def partB(input):
    windowSum = sum([input[i] for i in range(3)])
    count = 0
    for i in range(3, len(input)):
        tmp = windowSum - input[i-3] + input[i]
        if tmp > windowSum:
            count += 1
        windowSum = tmp
    return count


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
