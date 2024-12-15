import re

def t(grid):
    '''Tranpose the grid of strings into a new grid of strings'''
    return list(map(''.join, zip(*grid)))

def move_left(grid):
    pattern = r"\.O*@"
    replacement = lambda m: f"{m.group().replace(".", "", 1)}."
    for i in range(len(grid)):
        if re.search(pattern, grid[i]):
            grid[i] = re.sub(pattern, replacement, grid[i])
    return grid

def move_right(grid):
    pattern = r"@O*\."
    replacement = lambda m: f".{m.group().replace(".", "", 1)}"
    for i in range(len(grid)):
        if re.search(pattern, grid[i]):
            grid[i] = re.sub(pattern, replacement, grid[i])
    return grid

def move_up(grid):
    return t(move_left(t(grid)))

def move_down(grid):
    return t(move_right(t(grid)))

def part_a(input):
    grid, moves = input.split("\n\n")
    grid = grid.splitlines()
    moves = ''.join(moves.split())
    for m in moves:
       match m:
            case "^":
                grid = move_up(grid)
            case "v":
                grid = move_down(grid)
            case "<":
                grid = move_left(grid)
            case ">":
                grid = move_right(grid)
            case _:
                print("invalid move")

    total = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "O":
                total += 100 * i + j
    return total

def part_b(input):
    grid, moves = input.split("\n\n")
    grid = grid.splitlines()
    moves = ''.join(moves.split())

    # Transform the grid
    new_grid = []
    for row in grid:
        tmp = list(row)
        tmp = [c.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.") for c in tmp]
        new_grid.append(''.join(tmp))

    grid = new_grid

    for row in grid:
        print(row)

