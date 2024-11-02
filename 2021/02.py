def part_a(input):
    data = [list(x.split(" ")) for x in input.splitlines()]
    x, y = 0, 0
    for row in data:
        dir, num = row[0], int(row[1])
        if dir == "forward":
            x += num
        elif dir == "down":
            y += num
        else:
            y -= num
    return x * y

def part_b(input):
    data = [list(x.split(" ")) for x in input.splitlines()]
    x, y, aim = 0, 0, 0

    for row in data:
        dir, num = row[0], int(row[1])
        if dir == "forward":
            x += num
            y += aim * num
        elif dir == "down":
            aim += num
        else:
            aim -= num
    return x * y
