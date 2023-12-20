def part_a(input):
    data = [tuple(row.split(' ')) for row in input.splitlines()]
    grid_data = {}
    area = 0
    perimeter = 0
    start = (0, 0)
    end = (0, 0)
    for d, l, _ in data:
        l = int(l)
        perimeter += l
        if d == 'R':
            end = (start[0], start[1] + l)
        elif d == 'L':
            end = (start[0], start[1] - l)
        elif d == 'U':
            end = (start[0] - l, start[1])
        else:
            end = (start[0] + l, start[1])
        area += start[0] * end[1] - start[1] * end[0]
        start = end

    area = abs(area) // 2
    interior = area - perimeter // 2 + 1
    return perimeter + interior

def part_b(input):
    data = [tuple(row.split(' ')) for row in input.splitlines()]
    grid_data = {}
    area = 0
    perimeter = 0
    start = (0, 0)
    end = (0, 0)
    for _, l, h in data:
        h = h.rstrip(')').lstrip('(').lstrip('#')
        l = int(h[0:-1], 16)
        if h[-1] == '0':
            d = 'R'
        elif h[-1] == '1':
            d = 'D'
        elif h[-1] == '2':
            d = 'L'
        else:
            d = 'U'

        perimeter += l
        if d == 'R':
            end = (start[0], start[1] + l)
        elif d == 'L':
            end = (start[0], start[1] - l)
        elif d == 'U':
            end = (start[0] - l, start[1])
        else:
            end = (start[0] + l, start[1])
        area += start[0] * end[1] - start[1] * end[0]
        start = end

    area = abs(area) // 2
    interior = area - perimeter // 2 + 1
    return perimeter + interior
