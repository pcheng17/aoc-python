from functools import reduce
import operator

def parse(input):
    group1, group2 = input.split('\n\n')

    group1 = group1.split('\n')
    group2 = group2.split('\n')

    workflows = {}
    for line in group1:
        k, v = line.split('{')
        v = v.rstrip('}')
        parts = v.split(',')
        workflows[k] = []
        for part in parts:
            if ':' in part:
                condition, action = part.split(':')
                if '<' in condition:
                    lhs, rhs = condition.split('<')
                    workflows[k].append((lhs, operator.lt, int(rhs), action))
                else:
                    lhs, rhs = condition.split('>')
                    workflows[k].append((lhs, operator.gt, int(rhs), action))
            else:
                workflows[k].append(part)

    parts = []
    for line in group2:
        line = line.lstrip('{').rstrip('}')
        tmp = {}
        for x in line.split(','):
            lhs, rhs = x.split('=')
            tmp[lhs] = int(rhs)
        parts.append(tmp)

    return workflows, parts

def recurse(workflows, ranges, node):
    if node == 'A':
        total = 1
        for r in ranges.values():
            total *= r[1] - r[0]
        return total
    if node == 'R':
        return 0

    total = 0
    next_ranges = {k: v for k, v in ranges.items()}
    for fn in workflows[node]:
        if isinstance(fn, tuple):
            lhs, op, rhs, action = fn
            a, b = ranges[lhs]
            if op == operator.lt:
                ranges[lhs] = (a, rhs)
                next_ranges[lhs] = (rhs, b)
            else:
                ranges[lhs] = (rhs+1, b)
                next_ranges[lhs] = (a, rhs+1)
            total += recurse(workflows, ranges, action)
            ranges = {k: v for k, v in next_ranges.items()}
        else:
            total += recurse(workflows, ranges, fn)

    return total

def part_a(input):
    workflows, parts = parse(input)

    total = 0
    for part in parts:
        node = 'in'
        while node != 'A' and node != 'R':
            for fn in workflows[node]:
                if isinstance(fn, tuple):
                    lhs, op, rhs, action = fn
                    if op(part[lhs], rhs):
                        node = action
                        break
                else:
                    node = fn
        if node == 'A':
            total += sum(part.values())
    return total


def part_b(input):
    group1, _ = input.split('\n\n')
    group1 = group1.split('\n')

    workflows = {}
    for line in group1:
        k, v = line.split('{')
        v = v.rstrip('}')
        parts = v.split(',')
        workflows[k] = []
        for part in parts:
            if ':' in part:
                condition, action = part.split(':')
                if '<' in condition:
                    lhs, rhs = condition.split('<')
                    workflows[k].append((lhs, operator.lt, int(rhs), action))
                else:
                    lhs, rhs = condition.split('>')
                    workflows[k].append((lhs, operator.gt, int(rhs), action))
            else:
                workflows[k].append(part)

    ranges = { 'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001) }

    return recurse(workflows, ranges, 'in')


