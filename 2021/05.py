from collections import defaultdict

def part_a(input):
    touched = defaultdict(int)
    for row in input.split('\n'):
        a, b = row.split(' -> ')
        start = tuple(map(int, a.split(',')))
        end = tuple(map(int, b.split(',')))
        if start[0] == end[0]:
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                touched[(start[0], y)] += 1
        if start[1] == end[1]:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                touched[(x, start[1])] += 1

    return len([x for x in touched.values() if x > 1])

def part_b(input):
    touched = defaultdict(int)
    for row in input.split('\n'):
        a, b = row.split(' -> ')
        start = tuple(map(int, a.split(',')))
        end = tuple(map(int, b.split(',')))
        deltax = end[0] - start[0]
        deltay = end[1] - start[1]
        dx = 1 if deltax > 0 else -1
        dy = 1 if deltay > 0 else -1
        if start[0] == end[0]:
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                touched[(start[0], y)] += 1
        elif start[1] == end[1]:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                touched[(x, start[1])] += 1
        else:
            for (x,y) in zip(range(start[0], end[0]+dx, dx), range(start[1], end[1]+dy, dy)):
                touched[(x, y)] += 1

    return len([x for x in touched.values() if x > 1])
