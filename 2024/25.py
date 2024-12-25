def part_a(input):
    data = input.split('\n\n')
    keys = []
    locks = []
    for x in data:
        rows = x.split('\n')
        if all(x == '#' for x in rows[0]):
            locks.append(rows)
        elif all(x == '#' for x in rows[-1]):
            keys.append(rows)

    key_heights = []
    lock_heights = []

    for lock in locks:
        z = list(zip(*lock))
        heights = []
        for row in z:
            heights.append(sum(1 for x in row if x == '#') - 1)
        lock_heights.append(heights)

    for key in keys:
        z = list(zip(*key))
        heights = []
        for row in z:
            heights.append(sum(1 for x in row if x == '#') - 1)
        key_heights.append(heights)

    total = 0
    for kh in key_heights:
        for lh in lock_heights:
            z = [x + y for x, y in zip(kh, lh)]
            if all(t <= 5 for t in z):
                total += 1

    return total

def part_b(input):
    data = input.splitlines()
    return "Merry Christmas!"
