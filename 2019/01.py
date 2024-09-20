def getFuel(x):
    return x // 3 - 2

def part_a(input):
    data = [int(x) for x in input.splitlines()]
    return sum([getFuel(x) for x in data])

def part_b(input):
    data = [int(x) for x in input.splitlines()]
    fuel = 0
    for x in data:
        y = getFuel(x)
        fuel += y
        while y > 0:
            y = getFuel(y)
            if y > 0:
                fuel += y
    return fuel
