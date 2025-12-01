def part_a(input):
    data = input.splitlines()
    turns = [(line[0], int(line[1:])) for line in data]

    dial = 50
    count = 0;

    for turn in turns:
        if turn[0] == 'L':
            dial -= turn[1]
        elif turn[0] == 'R':
            dial += turn[1]
        dial %= 100
        if dial == 0:
            count = count + 1

    return count



def part_b(input):
    data = input.splitlines()
    turns = [(line[0], int(line[1:])) for line in data]

    dial = 50
    count = 0;

    for turn in turns:
        old_dial = dial
        if turn[0] == 'L':
            dial -= turn[1]
        elif turn[0] == 'R':
            dial += turn[1]

        if old_dial * dial < 0:
            count = count + 1

        if dial == 0:
            dial = 100

        count = count + abs(dial) // 100
        dial %= 100

    return count
