def part_a(input):
    return sum((2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)
        for l, w, h in (map(int, line.split('x')) 
        for line in input.splitlines()))

def part_b(input):
    return sum(min(2 * (l + w), 2 * (w + h), 2 * (h + l)) + (l * w * h)
        for l, w, h in (map(int, line.split('x')) 
        for line in input.splitlines()))
