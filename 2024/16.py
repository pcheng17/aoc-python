from common.utils import is_inbounds

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

possible_dirs = {
    UP: (UP, LEFT, RIGHT),
    DOWN: (DOWN, LEFT, RIGHT),
    LEFT: (LEFT, UP, DOWN),
    RIGHT: (RIGHT, UP, DOWN)
}

BEST_A = None

def dfs(grid, pos, dir, points, seen):
    global BEST_A
    nr = len(grid)
    nc = len(grid[0])
    for d in possible_dirs[dir]:
        if d != dir:
            points += 1000
        dx, dy = d
        new_pos = (pos[0] + dx, pos[1] + dy)
        if is_inbounds(new_pos[0], new_pos[1], nr, nc):
            if grid[new_pos[0]][new_pos[1]] == "E":
                if BEST_A is None or points < BEST_A:
                    BEST_A = points
            elif grid[new_pos[0]][new_pos[1]] == ".":
                if (new_pos, d) not in seen:
                    seen[(new_pos, d)] = points
                    dfs(grid, new_pos, d, points, seen)
                else:
                    if points < seen[(new_pos, d)]:
                        dfs(grid, new_pos, d, points, seen)

def part_a(input):
    global BEST_A
    grid = [list(row) for row in input.splitlines()]

    S = None
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                S = (i, j)

    seen = {}
    dfs(grid, S, RIGHT, 0, seen)
    return BEST_A





def part_b(input):
    data = input.splitlines()
