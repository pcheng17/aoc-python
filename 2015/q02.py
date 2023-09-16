from aocd import data


def parse(data):
    return data.splitlines()

def partA(input):
    return sum((2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)
        for l, w, h in (map(int, line.split('x')) 
        for line in input))

def partB(input):
    return sum(min(2 * (l + w), 2 * (w + h), 2 * (h + l)) + (l * w * h)
        for l, w, h in (map(int, line.split('x')) 
        for line in input))

def solveA(input):
    return partA(input)

def solveB(input):
    return partB(input)

if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
