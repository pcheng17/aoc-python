from collections import defaultdict
import re

def part_a(input):
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

def get_above_and_below(grid, block_pos, coord_to_block):
    whats_above = defaultdict(list)
    whats_below = defaultdict(list)
    for k, v in block_pos.items():
        above_left = (v[0] - 1, v[1])
        above_right = (v[0] - 1, v[1] + 1)
        below_left = (v[0] + 1, v[1])
        below_right = (v[0] + 1, v[1] + 1)
        if above_left in coord_to_block:
            whats_above[k].append(coord_to_block[above_left])
        elif grid[above_left[0]][above_left[1]] == "#":
            whats_above[k].append(-1)
        if below_left in coord_to_block:
            whats_below[k].append(coord_to_block[below_left])
        elif grid[below_left[0]][below_left[1]] == "#":
            whats_below[k].append(-1)
        if above_right in coord_to_block:
            whats_above[k].append(coord_to_block[above_right])
        elif grid[above_right[0]][above_right[1]] == "#":
            whats_above[k].append(-1)
        if below_right in coord_to_block:
            whats_below[k].append(coord_to_block[below_right])
        elif grid[below_right[0]][below_right[1]] == "#":
            whats_below[k].append(-1)
    return whats_above, whats_below

def get_block_coord_maps(grid):
    block_pos = {}
    coord_to_block = {}
    block_id = 0
    for i, row in enumerate(grid):
        for match in re.finditer(r"\[\]", row):
            block_pos[block_id] = (i, match.start())
            coord_to_block[(i, match.start())] = block_id
            coord_to_block[(i, match.start() + 1)] = block_id
            block_id += 1
    return block_pos, coord_to_block

def part_b(input):
    def move_left(grid):
        pattern = r"\.(\[\])*@"
        replacement = lambda m: f"{m.group().replace(".", "", 1)}."
        for i in range(len(grid)):
            if re.search(pattern, grid[i]):
                grid[i] = re.sub(pattern, replacement, grid[i])
        return grid

    def move_right(grid):
        pattern = r"@(\[\])*\."
        replacement = lambda m: f".{m.group().replace(".", "", 1)}"
        for i in range(len(grid)):
            if re.search(pattern, grid[i]):
                grid[i] = re.sub(pattern, replacement, grid[i])
        return grid

    def can_move_up(idx, above_map, block_pos):
        for above in above_map[idx]:
            if -1 in above:
                return False
            else:
                if above[0] == above[1]:
                    return can_move_up(above[0], above_map, block_pos)
                else:
                    return can_move_up(above[0], above_map, block_pos) and can_move_up(above[1], above_map, block_pos)

    def can_move_down(idx, below_map, block_pos):
        for below in below_map[idx]:
            if -1 in below:
                return False
            else:
                if below[0] == below[1]:
                    return can_move_down(below[0], below_map, block_pos)
                else:
                    return can_move_down(below[0], below_map, block_pos) and can_move_down(below[1], below_map, block_pos)

    def get_current_pos(grid):
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "@":
                    return (i, j)
        return (-1, -1)

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

    block_pos, coord_to_block = get_block_coord_maps(grid)
    whats_above, whats_below = get_above_and_below(grid, block_pos, coord_to_block)

    for m in moves:
       match m:
            case "^":
                curr_pos = get_current_pos(grid)
                above_pos = (curr_pos[0] - 1, curr_pos[1])
                if above_pos in coord_to_block:
                    if can_move_up(coord_to_block[above_pos], whats_above, block_pos):
                        # Move up
                        pass
            case "v":
                curr_pos = get_current_pos(grid)
                below_pos = (curr_pos[0] + 1, curr_pos[1])
                if below_pos in coord_to_block:
                    if can_move_down(coord_to_block[below_pos], whats_below, block_pos):
                        # Move down
                        pass
            case "<":
                grid = move_left(grid)
            case ">":
                grid = move_right(grid)
            case _:
                print("invalid move")

