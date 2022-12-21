from aocd import data


test = '''
1
2
-3
3
-2
0
4
'''

DECRYPTION = 811589153


def parse(data):
    return [int(x) for x in data.strip().splitlines()]


def mix(input: list[int], indexed_input: list[tuple[int, int]]):
    for i in range(len(indexed_input)):
        n = input[i]
        bIdx = indexed_input.index((i, n))
        eIdx = (bIdx + n) % (len(indexed_input) - 1)
        if bIdx < eIdx:
            indexed_input[bIdx : eIdx] = indexed_input[bIdx + 1 : eIdx + 1]
        elif bIdx > eIdx:
            indexed_input[eIdx + 1 : bIdx + 1] = indexed_input[eIdx : bIdx]
        indexed_input[eIdx] = (i, n)


def partA(input: list[int]):
    indexed_input = [(idx, n) for idx, n in enumerate(input)]
    length = len(indexed_input)
    mix(input, indexed_input)
    zeroIdx = next(idx for idx, x in enumerate(indexed_input) if x[1] == 0)
    return sum([indexed_input[(zeroIdx + n) % length][1] for n in [1000, 2000, 3000]])


def partB(input: list[int]):
    decrypted_input = [DECRYPTION * x for x in input]
    indexed_input = [(idx, n) for idx, n in enumerate(decrypted_input)]
    length = len(indexed_input)
    for _ in range(10):
        mix(decrypted_input, indexed_input)
    zeroIdx = next(idx for idx, x in enumerate(indexed_input) if x[1] == 0)
    return sum([indexed_input[(zeroIdx + n) % length][1] for n in [1000, 2000, 3000]])


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
