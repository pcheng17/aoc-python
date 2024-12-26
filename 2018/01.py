from itertools import cycle

def part_a(input):
    return sum(int(x) for x in input.splitlines())

def part_b(input):
    seen = set()
    freq = 0
    for x in cycle(int(x) for x in input.splitlines()):
        freq += x
        if freq in seen:
            return freq
        seen.add(freq)

