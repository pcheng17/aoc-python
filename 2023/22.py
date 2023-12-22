from collections import defaultdict

def is_lt(a, b):
    if a[2] < b[2]:
        return True
    elif a[2] > b[2]:
        return False
    else:
        if a[1] < b[1]:
            return True
        elif a[1] > b[1]:
            return False
        else:
            if a[0] < b[0]:
                return True
            elif a[0] > b[0]:
                return False
            else:
                return False

def overlap(r1, r2):
    return r1[0] <= r2[1] and r2[0] <= r1[1]

def support(b1, b2):
    return overlap((b1[0][0], b1[1][0]), (b2[0][0], b2[1][0])) and overlap((b1[0][1], b1[1][1]), (b2[0][1], b2[1][1]))

def is_only_child(p2c, b):
    return any(b in v and len(v) == 1 for v in p2c.values())

def simulate(bricks):
    surface = defaultdict(lambda: 0)
    fallen_bricks = []
    for a, b, idx in bricks:
        highest = max(surface[(i, j)] for i in range(a[0], b[0] + 1) for j in range(a[1], b[1] + 1))
        new_highest = highest + (b[2] - a[2] + 1)
        for i in range(a[0], b[0] + 1):
            for j in range(a[1], b[1] + 1):
                surface[(i, j)] = new_highest
        fallen_bricks.append(((a[0], a[1], highest + 1), (b[0], b[1], new_highest), idx))
    return fallen_bricks

def part_a(input):
    data = input.splitlines()
    bricks = []
    for i, row in enumerate(data):
        a, b = row.split('~')
        at = tuple(map(int, a.split(',')))
        bt = tuple(map(int, b.split(',')))
        if is_lt(at, bt):
            bricks.append((at, bt, i))
        else:
            bricks.append((bt, at, i))

    bricks.sort(key=lambda x: x[0][2])

    fallen_bricks = simulate(bricks)

    min_height = min(x[0][2] for x in fallen_bricks)
    max_height = max(x[1][2] for x in fallen_bricks)

    height_map = defaultdict(list)
    for h in range(min_height, max_height + 1):
        for b in fallen_bricks:
            if b[0][2] <= h <= b[1][2]:
                height_map[h].append(b)

    can_remove = set()
    for h in range(max_height, min_height, -1):
        ht = height_map[h] # list of bricks
        hb = height_map[h-1] # list of bricks

        # Construct a graph of dependencies
        p2c = defaultdict(list)
        for bt in ht:
            p2c[bt].extend([bb for bb in hb if support(bt, bb)])

        # Find bricks that can be removed
        can_remove.update([bb for bb in hb if not is_only_child(p2c, bb)])

    for b in height_map[max_height]:
        can_remove.add(b)

    can_remove_list = list(can_remove)
    can_remove_list.sort(key=lambda x: x[2])
    return len(can_remove)

def part_b(input):
    data = input.splitlines()
    bricks = []
    for i, row in enumerate(data):
        a, b = row.split('~')
        at = tuple(map(int, a.split(',')))
        bt = tuple(map(int, b.split(',')))
        if is_lt(at, bt):
            bricks.append((at, bt, i))
        else:
            bricks.append((bt, at, i))
    bricks.sort(key=lambda x: x[0][2])

    fallen_bricks = simulate(bricks)

    min_height = min(x[0][2] for x in fallen_bricks)
    max_height = max(x[1][2] for x in fallen_bricks)

    height_map = defaultdict(list)
    for h in range(min_height, max_height + 1):
        for b in fallen_bricks:
            if b[0][2] <= h <= b[1][2]:
                height_map[h].append(b)

    can_remove = set()
    for h in range(max_height, min_height, -1):
        ht = height_map[h] # list of bricks
        hb = height_map[h-1] # list of bricks

        # Construct a graph of dependencies
        p2c = defaultdict(list)
        for bt in ht:
            p2c[bt].extend([bb for bb in hb if support(bt, bb)])

        # Find bricks that can be removed
        can_remove.update([bb for bb in hb if not is_only_child(p2c, bb)])

    for b in height_map[max_height]:
        can_remove.add(b)

    to_disintegrate = [b for b in fallen_bricks if b not in can_remove]
    fallen_bricks_set = set(fallen_bricks)

    total = 0
    for b in to_disintegrate:
        new_bricks_set = set(simulate([brick for brick in fallen_bricks if brick != b]))
        total += (len(fallen_bricks_set - new_bricks_set) - 1)

    return total







