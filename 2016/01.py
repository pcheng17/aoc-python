def turn(facing, direction):
    directions = ['N', 'E', 'S', 'W']
    idx = directions.index(facing)
    if direction == 'R':
        idx = (idx + 1) % 4
    else:
        idx = (idx - 1) % 4
    return directions[idx]

def step(facing, start, steps):
    if facing == 'N':
        return (start[0], start[1] + steps)
    elif facing == 'E':
        return (start[0] + steps, start[1])
    elif facing == 'S':
        return (start[0], start[1] - steps)
    else:
        return (start[0] - steps, start[1])

def step_with_path(facing, start, steps):
    visited = set()
    if facing == 'N':
        for i in range(1, steps + 1):
            visited.add((start[0], start[1] + i))
        return (start[0], start[1] + steps), visited
    elif facing == 'E':
        for i in range(1, steps + 1):
            visited.add((start[0] + i, start[1]))
        return (start[0] + steps, start[1]), visited
    elif facing == 'S':
        for i in range(1, steps + 1):
            visited.add((start[0], start[1] - i))
        return (start[0], start[1] - steps), visited
    else:
        for i in range(1, steps + 1):
            visited.add((start[0] - i, start[1]))
        return (start[0] - steps, start[1]), visited

def part_a(input):
    data = input.split(', ')
    pos = (0, 0)
    facing = 'N'
    for x in data:
        facing = turn(facing, x[0])
        pos = step(facing, pos, int(x[1:]))
    return sum(map(abs, pos))

def part_b(input):
    data = input.split(', ')
    pos = (0, 0)
    facing = 'N'
    visited = set()
    visited.add(pos)
    for x in data:
        facing = turn(facing, x[0])
        pos, path = step_with_path(facing, pos, int(x[1:]))
        for y in path:
            if y in visited:
                return sum(map(abs, y))
            visited.add(y)
