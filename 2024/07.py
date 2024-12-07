def test_for_a(values, target):
    if len(values) == 1:
        if values[0] == target:
            return True
        else:
            return False

    tmp = []
    tmp.append(values[0]+values[1])
    tmp.extend(values[2:])
    if test_for_a(tmp, target):
        return True

    tmp = []
    tmp.append(values[0]*values[1])
    tmp.extend(values[2:])
    if test_for_a(tmp, target):
        return True

    return False

def test_for_b(values, target):
    if len(values) == 1:
        if values[0] == target:
            return True
        else:
            return False

    tmp = []
    tmp.append(values[0]+values[1])
    tmp.extend(values[2:])
    if test_for_b(tmp, target):
        return True

    tmp = []
    tmp.append(values[0]*values[1])
    tmp.extend(values[2:])
    if test_for_b(tmp, target):
        return True

    tmp = []
    tmp.append(int(str(values[0]) + str(values[1])))
    tmp.extend(values[2:])
    if test_for_b(tmp, target):
        return True

    return False


def part_a(input):
    data = input.splitlines()
    total = 0
    for row in data:
        test_value, values = row.split(':')
        test_value = int(test_value)
        values = list(map(int, values.strip().split(" ")))
        if test_for_a(values, test_value):
            total += test_value
    return total


def part_b(input):
    data = input.splitlines()
    total = 0
    for row in data:
        test_value, values = row.split(':')
        test_value = int(test_value)
        values = list(map(int, values.strip().split(" ")))
        if test_for_b(values, test_value):
            total += test_value
    return total
