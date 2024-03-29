def part_a(input):
    data = input.splitlines()
    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    for c in data[0]:
        match c:
            case '^': y += 1
            case 'v': y -= 1
            case '>': x += 1
            case '<': x -= 1
        visited.add((x, y))
    return len(visited)

def part_b(input):
    data = input.splitlines()
    visited = set()
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited.add((robo_x, robo_y))
    for i, c, in enumerate(data[0]):
        if i % 2 == 0:
            match c:
                case '^': santa_y += 1
                case 'v': santa_y -= 1
                case '>': santa_x += 1
                case '<': santa_x -= 1
            visited.add((santa_x, santa_y))
        else:
            match c:
                case '^': robo_y += 1
                case 'v': robo_y -= 1
                case '>': robo_x += 1
                case '<': robo_x -= 1
            visited.add((robo_x, robo_y))
    return len(visited)
