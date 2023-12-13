from functools import cache

def can_fit(spring, window):
    for x, y in zip(spring, window):
        if (x == '.' and y == '#') or (x == '#' and y == '.'):
            return False
    return True

@cache
def dp(spring, config, i, j):
    spr = spring[i:]
    cfg = config[j:]

    if i == len(spring) and j == len(config):
        return 1

    if j == len(config):
        return 0 if '#' in spr else 1

    if len(spr) < sum(config[j:]):
        return 0

    if len(cfg) == 1:
        window = '#' * cfg[0]
    else:
        window = '#' * cfg[0] + '.'
    
    total = 0
    for k in range(len(spr) - len(window) + 1):
        if can_fit(spr[k:k+len(window)], window):
            total += dp(spring, config, i + k + len(window), j + 1)
        if spr[k] == '#':
            break
    return total

def part_a(input):
    data = input.splitlines()
    total = 0
    for row in data:
        spring, config = row.split(' ')
        config = tuple(int(c) for c in config.split(','))
        total += dp(spring, config, 0, 0)
    return total

def part_b(input):
    data = input.splitlines()
    total = 0
    for row in data:
        spring, config = row.split(' ')
        config = [int(c) for c in config.split(',')]
        total += dp('?'.join([spring] * 5), tuple(config * 5), 0, 0)
    return total
