from aocd import get_data
raw_data = get_data(day=1, year=2015)

def parse(data):
    return data.splitlines()

def part_a(input):
    return sum(1 if c == '(' else -1 for c in input[0])

def part_b(input):
    floor = 0
    for i, c in enumerate(input[0]):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i + 1
