def part_a(input):
    return sum(1 if c == '(' else -1 for c in input.splitlines()[0])

def part_b(input):
    floor = 0
    for i, c in enumerate(input.splitlines()[0]):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i + 1
