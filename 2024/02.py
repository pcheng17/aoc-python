def is_safe(row):
    diff = [y - x for x, y in zip(row[0:-1], row[1:])]
    incCheck = all(x >= 1 and x <= 3 for x in diff)
    decCheck = all(x >= -3 and x <= -1 for x in diff)
    return incCheck or decCheck

def is_safe_b(row):
    if is_safe(row):
        return True
    for i in range(len(row)):
        if is_safe(row[0:i] + row[i+1:]):
            return True
    return False

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
