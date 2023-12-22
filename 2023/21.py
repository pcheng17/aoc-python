import numpy as np

def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def part_a(input):
    grid = input.splitlines()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)

    frontier = set()
    frontier.add(start)

    for steps in range(64):
        new_frontier = set()
        for i, j in frontier:
            if in_bounds(grid, i+1, j) and grid[i+1][j] != '#':
                new_frontier.add((i+1, j))
            if in_bounds(grid, i-1, j) and grid[i-1][j] != '#':
                new_frontier.add((i-1, j))
            if in_bounds(grid, i, j+1) and grid[i][j+1] != '#':
                new_frontier.add((i, j+1))
            if in_bounds(grid, i, j-1) and grid[i][j-1] != '#':
                new_frontier.add((i, j-1))
        frontier = new_frontier

    return len(frontier)



def part_b(input):
    grid = input.splitlines()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)

    steps = 26501365

    rows = len(grid)
    cols = len(grid[0])

    frontier = set()
    frontier.add(start)

    values = []
    for step in range(600):
        new_frontier = set()
        for i, j in frontier:
            if grid[(i+1) % rows][j % cols] != '#':
                new_frontier.add((i+1, j))
            if grid[(i-1) % rows][j % cols] != '#':
                new_frontier.add((i-1, j))
            if grid[i % rows][(j+1) % cols] != '#':
                new_frontier.add((i, j+1))
            if grid[i % rows][(j-1) % cols] != '#':
                new_frontier.add((i, j-1))

        values.append(len(new_frontier))
        frontier = new_frontier

    ys = [v for i, v in enumerate(values, 1) if i % rows == 65]
    xs = list(range(len(ys)))
    model = np.poly1d(np.polyfit(xs, ys, 2))
    return floor(np.polyval(model, steps // rows))
