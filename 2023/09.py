def diff(a):
    return [y - x for x, y in zip(a[0:-1], a[1:])]

def solve(numbers):
    t = 0
    for row in numbers:
        d = [row]
        while any(d[-1]):
            d.append(diff(d[-1]))
        t += sum(r[-1] for r in d)
    return t

def part_a(input):
    numbers = [list(map(int, line.split())) for line in input.splitlines()]
    return solve(numbers)

def part_b(input):
    numbers = [list(reversed(list(map(int, line.split())))) for line in input.splitlines()]
    return solve(numbers)
