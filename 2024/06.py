def part_a(input):
    data = input.splitlines()
    si = 0
    sj = 0
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "^":
                si = i
                sj = j
                break
    obstacles = set()
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "#":
                obstacles.add((i, j))

    visited = set()

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    dir = UP

    ci = si
    cj = sj

    while 0 <= ci < len(data) and 0 <= cj < len(data[0]):
        visited.add((ci, cj))
        if (ci + dir[0], cj + dir[1]) in obstacles:
            if dir == UP:
                dir = RIGHT
            elif dir == RIGHT:
                dir = DOWN
            elif dir == DOWN:
                dir = LEFT
            else:
                dir = UP
        else:
            ci = ci + dir[0]
            cj = cj + dir[1]

    return len(visited)

def part_b(input):
    data = input.splitlines()
    grid = [list(row) for row in data]
    si = 0
    sj = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "^":
                si = i
                sj = j
                break
    obstacles = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "#":
                obstacles.add((i, j))

    visited = set()

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    dir = UP

    ci = si
    cj = sj

    while 0 <= ci < len(grid) and 0 <= cj < len(grid[0]):
        visited.add((ci, cj))
        if (ci + dir[0], cj + dir[1]) in obstacles:
            if dir == UP:
                dir = RIGHT
            elif dir == RIGHT:
                dir = DOWN
            elif dir == DOWN:
                dir = LEFT
            else:
                dir = UP
        else:
            ci = ci + dir[0]
            cj = cj + dir[1]

    visited.remove((si, sj))

    total = 0
    for ni, nj in visited:
        revisited = set()
        obstacles.add((ni, nj))
        ci = si
        cj = sj
        dir = UP
        while 0 <= ci < len(data) and 0 <= cj < len(data[0]):
            if (ci, cj, dir) in revisited:
                total = total + 1
                break
            revisited.add((ci, cj, dir))
            a = ci + dir[0]
            b = cj + dir[1]
            if (a, b) in obstacles:
                if dir == UP:
                    dir = RIGHT
                elif dir == RIGHT:
                    dir = DOWN
                elif dir == DOWN:
                    dir = LEFT
                else:
                    dir = UP
            else:
                ci = ci + dir[0]
                cj = cj + dir[1]

        obstacles.remove((ni, nj))

    return total

