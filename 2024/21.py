import itertools
import functools

keypad_to_coord = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2),
}

wasd_to_coord = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2)
}

dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

@functools.lru_cache(maxsize=None)
def recurse(string, depth, current, use_wasd):
    if not string:
        return 0

    mapping = wasd_to_coord if use_wasd else keypad_to_coord

    i, j = current
    ei, ej = mapping[string[0]]

    dx, dy = ei - i, ej - j
    moves = 'v' * dx if dx > 0 else '^' * -dx
    moves += '>' * dy if dy > 0 else '<' * -dy

    if depth == 0:
        return len(moves) + 1 + recurse(string[1:], depth, (ei, ej), use_wasd)

    zzzz = []
    perms = set([''.join(x) for x in itertools.permutations(moves)])
    for perm in perms:
        x, y = i, j
        for move in perm:
            dx, dy = dirs[move]
            x, y = x + dx, y + dy
            if (x, y) not in mapping.values():
                break
        else:
            zzzz.append(recurse(perm + 'A', depth - 1, wasd_to_coord['A'], True))

    return min(zzzz) + recurse(string[1:], depth, (ei, ej), use_wasd)

def solve(codes, depth):
    total = 0
    for code in codes:
        numcode = int(''.join([c for c in code if c.isdigit()]))
        length = recurse(code, depth, keypad_to_coord['A'], False)
        total += numcode * length
    return total

def part_a(input):
    data = input.splitlines()
    return solve(data, 2)

def part_b(input):
    data = input.splitlines()
    return solve(data, 25)
