def is_safe(row):
    diff = [y - x for x, y in zip(row[0:-1], row[1:])]
    incCheck = all(x >= 1 and x <= 3 for x in diff)
    decCheck = all(x >= -3 and x <= -1 for x in diff)
    return incCheck or decCheck

def is_safe_b(row):
    sf = is_safe(row)
    for i in range(len(row)):
        tmp = row.copy()
        tmp.pop(i)
        sf = sf or is_safe(tmp)
    return sf

def part_a(input):
    data = input.splitlines()
    out = 0
    for row in data:
        nums = [int(x) for x in row.split(' ')]
        out = out + int(is_safe(nums))
    return out

def part_b(input):
    data = input.splitlines()
    out = 0
    for row in data:
        nums = [int(x) for x in row.split(' ')]
        out = out + int(is_safe_b(nums))
    return out
