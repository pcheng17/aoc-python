import re

def det(a, b, c, d):
    return a*d - b*c

def part_a(input):
    data = input.split("\n\n")
    total = 0
    for block in data:
        rows = block.splitlines()
        buttonA = list(map(int, re.findall(r"\d+", rows[0])))
        buttonB = list(map(int, re.findall(r"\d+", rows[1])))
        goal = list(map(int, re.findall(r"\d+", rows[2])))
        denom = det(buttonA[0], buttonB[0], buttonA[1], buttonB[1])
        a = det(goal[0], buttonB[0], goal[1], buttonB[1]) / denom
        b = det(buttonA[0], goal[0], buttonA[1], goal[1]) / denom
        if int(a) == a and int(b) == b and a >= 0 and b >= 0 and a <= 100 and b <= 100:
            total += (3 * a + b)
    return int(total)


def part_b(input):
    data = input.split("\n\n")
    total = 0
    for block in data:
        rows = block.splitlines()
        buttonA = list(map(int, re.findall(r"\d+", rows[0])))
        buttonB = list(map(int, re.findall(r"\d+", rows[1])))
        goal = [x + 10000000000000 for x in map(int, re.findall(r"\d+", rows[2]))]
        denom = det(buttonA[0], buttonB[0], buttonA[1], buttonB[1])
        a = det(goal[0], buttonB[0], goal[1], buttonB[1]) / denom
        b = det(buttonA[0], goal[0], buttonA[1], goal[1]) / denom
        if int(a) == a and int(b) == b and a >= 0 and b >= 0:
            total += (3 * a + b)
    return int(total)
