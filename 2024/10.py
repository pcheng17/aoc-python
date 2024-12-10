from common.utils import is_inbounds

def part_a(input):
    data = input.splitlines()
    grid = [list(map(int, list(row))) for row in data]

    trailheads = []
    trailends = []
    nr = len(grid)
    nc = len(grid[0])

    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == 0:
                trailheads.append((i, j))
            if grid[i][j] == 9:
                trailends.append((i, j))

    print(f"Number of trailheads: {len(trailheads)}")

    scores = [[0] * nc for _ in range(nr)]

    # BFS from each trailend
    for pos in trailends:
        frontier = [pos]
        visited = set()
        while frontier:
            new_frontier = []
            for pos in frontier:
                i, j = pos
                height = grid[i][j]
                visited.add(pos)
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if is_inbounds(ni, nj, nr, nc) and grid[ni][nj] == (height-1) and (ni, nj) not in visited:
                        new_frontier.append((ni, nj))
            frontier = new_frontier
        for pos in visited:
            scores[pos[0]][pos[1]] += 1

    total = 0
    for i, j in trailheads:
        total += scores[i][j]

    return total

def part_b(input):
    data = input.splitlines()
    grid = [list(map(int, list(row))) for row in data]

    trailheads = []
    trailends = []
    nr = len(grid)
    nc = len(grid[0])

    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == 0:
                trailheads.append((i, j))
            if grid[i][j] == 9:
                trailends.append((i, j))

    print(f"Number of trailheads: {len(trailheads)}")

    def dfs(pos, grid, count):
        height = grid[pos[0]][pos[1]]
        if grid[pos[0]][pos[1]] == 9:
            count[0] += 1
            return
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = pos[0] + di, pos[1] + dj
            if is_inbounds(ni, nj, nr, nc) and grid[ni][nj] == height + 1:
                dfs((ni, nj), grid, count)

    # For each trailhead, I need to find the number of paths to every possible trailend
    counts = [0]
    for pos in trailheads:
        dfs(pos, grid, counts)

    return counts[0]

