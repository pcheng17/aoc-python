def part_a(input):
    data = input.splitlines()
    total = 0
    left = []
    right = []
    for row in data:
        x, y = row.split('   ')
        left.append(int(x))
        right.append(int(y))

    left = sorted(left)
    right = sorted(right)

    total = sum([abs(x-y) for x, y in zip(left, right)])
    return total


def part_b(input):
    data = input.splitlines()
    total = 0
    left = []
    right = []
    for row in data:
        x, y = row.split('   ')
        left.append(int(x))
        right.append(int(y))

    counts = [0] * (max(right)+1)
    for x in right:
        counts[x] = counts[x] + 1

    total = sum([x * counts[x] for x in left if x < len(counts)])
    return total
