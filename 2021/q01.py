from aocd import get_data
raw_data = get_data(day=1, year=2021)

def parse(data):
    return list(map(int, data.splitlines()))

def part_a(input):
    return sum([b > a for a, b in zip(input, input[1:])])

def part_b(input):
    windowSum = sum([input[i] for i in range(3)])
    count = 0
    for i in range(3, len(input)):
        tmp = windowSum - input[i-3] + input[i]
        if tmp > windowSum:
            count += 1
        windowSum = tmp
    return count
