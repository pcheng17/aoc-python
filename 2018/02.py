from itertools import combinations
from collections import defaultdict

def part_a(input):
    ans2 = 0
    ans3 = 0
    for line in input.splitlines():
        counts = defaultdict(int)
        for c in line:
            counts[c] += 1
        found_two = any(v == 2 for v in counts.values())
        found_three = any(v == 3 for v in counts.values())
        if found_two:
            ans2 += 1
        if found_three:
            ans3 += 1
    return ans2 * ans3

def part_b(input):
    data = [line for line in input.splitlines()]
    common = ''
    for a, b in combinations(data, 2):
        diffs = sum(1 for x, y in zip(a, b) if x != y)
        if diffs == 1:
            common = ''.join(x for x, y in zip(a, b) if x == y)
            break
    return common

