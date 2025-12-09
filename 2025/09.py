from itertools import combinations, pairwise

def part_a(input):
    data = []
    for row in input.splitlines():
        data.append([int(x) for x in row.split(',')])

    best_area = 0
    for (x, y), (u, v) in combinations(data, 2):
        x, u = sorted([x, u])
        y, v = sorted([y, v])
        area = (u - x + 1) * (v - y + 1)
        best_area = max(best_area, area)
    return best_area

def part_b(input):
    data = []
    for row in input.splitlines():
        data.append([int(x) for x in row.split(',')])

    best_area = -1
    for (x, y), (u, v) in combinations(data, 2):
        x, u = sorted([x, u])
        y, v = sorted([y, v])
        area = (u - x + 1) * (v - y + 1)
        bad = False
        for (a, b), (c, d) in pairwise(data + [data[0]]):
            a, c = sorted([a, c])
            b, d = sorted([b, d])
            if x < c and a < u and y < d and b < v:
                bad = True
                break
        if not bad:
            best_area = max(best_area, area)
    return best_area
