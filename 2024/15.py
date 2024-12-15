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

def get_neighbor_lookup(grid, block_pos, coord_to_block):
    whats_above = defaultdict(list)
    whats_below = defaultdict(list)
    whats_left = defaultdict(list)
    whats_right = defaultdict(list)
    for k, v in enumerate(block_pos):
        above_left = (v[0] - 1, v[1])
        above_right = (v[0] - 1, v[1] + 1)
        below_left = (v[0] + 1, v[1])
        below_right = (v[0] + 1, v[1] + 1)
        left = (v[0], v[1] - 1)
        right = (v[0], v[1] + 2)
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
        if left in coord_to_block:
            whats_left[k].append(coord_to_block[left])
        elif grid[left[0]][left[1]] == "#":
            whats_left[k].append(-1)
        if right in coord_to_block:
            whats_right[k].append(coord_to_block[right])
        elif grid[right[0]][right[1]] == "#":
            whats_right[k].append(-1)
    return whats_above, whats_below, whats_left, whats_right

def get_block_coord_maps(grid):
    block_pos = []
    coord_to_block = {}
    block_id = 0
    for i, row in enumerate(grid):
        for match in re.finditer(r"\[\]", row):
            block_pos.append((i, match.start()))
            coord_to_block[(i, match.start())] = block_id
            coord_to_block[(i, match.start() + 1)] = block_id
            block_id += 1
    return block_pos, coord_to_block

def part_b(input):
    def get_assembly_recursive(idx, dmap, assembly):
        if idx in dmap:
            tmp = dmap[idx]
            if -1 in tmp:
                return False
            else:
                if (len(tmp) == 2 and tmp[0] == tmp[1]) or len(tmp) == 1:
                    assembly.append(tmp[0])
                    return get_assembly_recursive(tmp[0], dmap, assembly)
                else:
                    assembly.extend(tmp)
                    return get_assembly_recursive(tmp[0], dmap, assembly) and get_assembly_recursive(tmp[1], dmap, assembly)
        return True

    def move_up(grid, curr_pos):
        def get_assembly_above(pos):
            assembly = []
            can_move = True
            above_pos = (pos[0] - 1, pos[1])
            if above_pos in coord_to_block:
                block_idx = coord_to_block[above_pos]
                assembly.append(block_idx)
                can_move = get_assembly_recursive(block_idx, above_map, assembly)
            return assembly, can_move

        assembly, can_move = get_assembly_above(curr_pos)
        if not assembly:
            new_pos = (curr_pos[0] - 1, curr_pos[1])
            if grid[new_pos[0]][new_pos[1]] == ".":
                return draw_grid(grid, curr_pos, new_pos, block_pos, block_pos)
            else:
                can_move = False
        if can_move:
            block_pos_old = block_pos.copy()
            for idx in assembly:
                block_pos[idx] = (block_pos[idx][0] - 1, block_pos[idx][1])
            new_pos = (curr_pos[0] - 1, curr_pos[1])
            return draw_grid(grid, curr_pos, new_pos, block_pos_old, block_pos)
        return grid

    def move_down(grid, curr_pos):
        def get_assembly_below(pos):
            assembly = []
            can_move = True
            below_pos = (pos[0] + 1, pos[1])
            if below_pos in coord_to_block:
                block_idx = coord_to_block[below_pos]
                assembly.append(block_idx)
                can_move = get_assembly_recursive(block_idx, below_map, assembly)
            return assembly, can_move

        assembly, can_move = get_assembly_below(curr_pos)
        if not assembly:
            new_pos = (curr_pos[0] + 1, curr_pos[1])
            if grid[new_pos[0]][new_pos[1]] == ".":
                return draw_grid(grid, curr_pos, new_pos, block_pos, block_pos)
            else:
                can_move = False
        if can_move:
            block_pos_old = block_pos.copy()
            for idx in assembly:
                block_pos[idx] = (block_pos[idx][0] + 1, block_pos[idx][1])
            new_pos = (curr_pos[0] + 1, curr_pos[1])
            return draw_grid(grid, curr_pos, new_pos, block_pos_old, block_pos)
        return grid

    def move_left(grid, curr_pos):
        def get_assembly_left(pos):
            assembly = []
            can_move = True
            left_pos = (pos[0], pos[1] - 1)
            if left_pos in coord_to_block:
                block_idx = coord_to_block[left_pos]
                assembly.append(block_idx)
                can_move = get_assembly_recursive(block_idx, left_map, assembly)
            return assembly, can_move

        assembly, can_move = get_assembly_left(curr_pos)
        if not assembly:
            new_pos = (curr_pos[0], curr_pos[1] - 1)
            if grid[new_pos[0]][new_pos[1]] == ".":
                return draw_grid(grid, curr_pos, new_pos, block_pos, block_pos)
            else:
                can_move = False
        if can_move:
            block_pos_old = block_pos.copy()
            for idx in assembly:
                block_pos[idx] = (block_pos[idx][0], block_pos[idx][1] - 1)
            new_pos = (curr_pos[0], curr_pos[1] - 1)
            return draw_grid(grid, curr_pos, new_pos, block_pos_old, block_pos)
        return grid

    def move_right(grid, curr_pos):
        def get_assembly_right(pos):
            assembly = []
            can_move = True
            right_pos = (pos[0], pos[1] + 1)
            if right_pos in coord_to_block:
                block_idx = coord_to_block[right_pos]
                assembly.append(block_idx)
                can_move = get_assembly_recursive(block_idx, right_map, assembly)
            return assembly, can_move

        assembly, can_move = get_assembly_right(curr_pos)
        if not assembly:
            new_pos = (curr_pos[0], curr_pos[1] + 1)
            if grid[new_pos[0]][new_pos[1]] == ".":
                return draw_grid(grid, curr_pos, new_pos, block_pos, block_pos)
            else:
                can_move = False
        if can_move:
            block_pos_old = block_pos.copy()
            for idx in assembly:
                block_pos[idx] = (block_pos[idx][0], block_pos[idx][1] + 1)
            new_pos = (curr_pos[0], curr_pos[1] + 1)
            return draw_grid(grid, curr_pos, new_pos, block_pos_old, block_pos)
        return grid

    def get_current_pos(grid):
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "@":
                    return (i, j)
        return (-1, -1)

    def draw_grid(grid, curr_pos, new_pos, block_pos_old, block_pos):
        tmp = [list(row) for row in grid]
        for (i, j) in block_pos_old:
            tmp[i][j] = "."
            tmp[i][j+1] = "."
        tmp[curr_pos[0]][curr_pos[1]] = "."
        for (i, j) in block_pos:
            tmp[i][j] = "["
            tmp[i][j+1] = "]"
        tmp[new_pos[0]][new_pos[1]] = "@"
        return [''.join(row) for row in tmp]

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
    # for row in grid:
    #     print(row)

    for m in moves:
        curr_pos = get_current_pos(grid)
        block_pos, coord_to_block = get_block_coord_maps(grid)
        above_map, below_map, left_map, right_map = get_neighbor_lookup(grid, block_pos, coord_to_block)
        match m:
            case "^":
                grid = move_up(grid, curr_pos)
            case "v":
                grid = move_down(grid, curr_pos)
            case "<":
                grid = move_left(grid, curr_pos)
            case ">":
                grid = move_right(grid, curr_pos)
            case _:
                print("invalid move")
        for row in grid:
            print(row)

    total = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "[":
                total += 100 * i + j
    return total

