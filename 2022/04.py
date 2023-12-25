def containsOther(x, y, u, v):
    return ((x<=u) and (y>=v))

def isRedundant(x, y, u, v):
    return containsOther(x, y, u, v) or containsOther(u, v, x, y)

def isOverlapping(x, y, u, v):
    return ((y>=u) and (v>=x))

def part_a(input):
    result = 0
    for line in input.splitlines():
        r1, r2 = line.split(',')
        r1a, r1b = map(int, r1.split('-'))
        r2a, r2b = map(int, r2.split('-'))
        result += int(isRedundant(r1a, r1b, r2a, r2b))
    return result

def part_b(input):
    result = 0
    for line in input.splitlines():
        r1, r2 = line.split(',')
        r1a, r1b = map(int, r1.split('-'))
        r2a, r2b = map(int, r2.split('-'))
        result += int(isOverlapping(r1a, r1b, r2a, r2b))
    return result
