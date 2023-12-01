from aocd import get_data
raw_data = get_data(day=2, year=2015)

def parse(data):
    return data.splitlines()

def part_a(input):
    return sum((2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)
        for l, w, h in (map(int, line.split('x')) 
        for line in input))

def part_b(input):
    return sum(min(2 * (l + w), 2 * (w + h), 2 * (h + l)) + (l * w * h)
        for l, w, h in (map(int, line.split('x')) 
        for line in input))
