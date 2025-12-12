def part_a(input):
    data = input.split("\n\n")

    shapes = []
    for i in range(len(data) - 1):
        shape = []
        z = data[i].splitlines()
        for j in range(1, len(z)):
            for k in range(len(z[j])):
                if z[j][k] == "#":
                    shape.append((j-1, k))
        shapes.append(shape)

    # That center spot can't be reached by anything else
    shapes[2].append((1, 1))

    tiles = []
    for row in data[-1].splitlines():
        size, reqs = row.split(": ")
        rows, cols = map(int, size.split("x"))
        reqs = list(map(int, reqs.split(" ")))
        tiles.append((rows, cols, reqs))

    candidate = set()
    for i, tile in enumerate(tiles):
        total_tiles = tile[0] * tile[1]
        coverage = sum(len(s) * t for s, t in zip(shapes, tile[2]))
        if coverage <= total_tiles:
            candidate.add(i)

    return len(candidate)

def part_b(input):
    return 'Merry Christmas!'
