from collections import defaultdict

def part_a(input):
    data = input.splitlines()
    # size of grid
    nr = len(data)
    nc = len(data[0])

    # First get all the unique antennas
    antennas = defaultdict(list)
    for i, row in enumerate(data):
        x = list(row)
        for j in range(len(x)):
            if x[j] != ".":
                antennas[x[j]].append((i, j))

    # For each unique antenna, I need to do a full pair-wise check for lines
    antinodes = set()
    for k, v in antennas.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                # Find slope between the two points
                dx = v[j][0] - v[i][0]
                dy = v[j][1] - v[i][1]
                # Position of first anti-node
                an1x = v[i][0] - dx
                an1y = v[i][1] - dy
                # Position of second anti-node
                an2x = v[j][0] + dx
                an2y = v[j][1] + dy
                if 0 <= an1x < nr and 0 <= an1y < nc:
                    antinodes.add((an1x, an1y))
                if 0 <= an2x < nr and 0 <= an2y < nc:
                    antinodes.add((an2x, an2y))

    return len(antinodes)

def part_b(input):
    data = input.splitlines()
    # size of grid
    nr = len(data)
    nc = len(data[0])

    # First get all the unique antennas
    antennas = defaultdict(list)
    for i, row in enumerate(data):
        x = list(row)
        for j in range(len(x)):
            if x[j] != ".":
                antennas[x[j]].append((i, j))

    # For each unique antenna, I need to do a full pair-wise check for lines
    antinodes = set()
    for k, v in antennas.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                antinodes.add((v[i][0], v[i][1]))
                antinodes.add((v[j][0], v[j][1]))

                # Find slope between the two points
                dx = v[j][0] - v[i][0]
                dy = v[j][1] - v[i][1]

                x = v[i][0]
                y = v[i][1]
                antinodes.add((v[i][0], v[i][1]))
                antinodes.add((v[j][0], v[j][1]))
                while True:
                    x -= dx
                    y -= dy
                    if 0 <= x < nr and 0 <= y < nc:
                        antinodes.add((x, y))
                    else:
                        break

                x = v[j][0]
                y = v[j][1]
                while True:
                    x += dx
                    y += dy
                    if 0 <= x < nr and 0 <= y < nc:
                        antinodes.add((x, y))
                    else:
                        break

    return len(antinodes)
