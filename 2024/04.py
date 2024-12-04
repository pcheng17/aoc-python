def get_count(text):
    return text.count("XMAS") + text.count("SAMX")

def part_a(input):
    data = input.splitlines()
    grid = []
    for row in data:
        grid.append(list(row))
    total = 0

    nr = len(grid)
    nc = len(grid[0])
    n = min(nr, nc)

    # Horizontals
    total = total + sum([get_count("".join(row)) for row in grid])

    # Verticals by tranposing the grid
    total = total + sum([get_count("".join(row)) for row in [*zip(*grid)]])

    # Main diagonal
    tmp = "".join([grid[i][i] for i in range(n)])
    total = total + get_count(tmp)

    # Off diagonals
    for i in range(1, len(grid)):
        tmp = "".join([grid[i+j][j] for j in range(n-i)])
        total = total + get_count(tmp)
        tmp = "".join([grid[j][i+j] for j in range(n-i)])
        total = total + get_count(tmp)

    # Rotate the grid 90 degrees
    rotated = [*zip(*grid[::-1])]

    # Main diagonal
    tmp = "".join([rotated[i][i] for i in range(n)])
    total = total + get_count(tmp)

    # Off diagonals
    for i in range(1, len(rotated)):
        tmp = "".join([rotated[i+j][j] for j in range(n-i)])
        total = total + get_count(tmp)
        tmp = "".join([rotated[j][i+j] for j in range(n-i)])
        total = total + get_count(tmp)

    return total

def part_b(input):
    data = input.splitlines()
    grid = []
    for row in data:
        grid.append(list(row))
    total = 0

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == "A":
                d1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
                d2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
                if (d1 == "SAM" or d1 == "MAS") and (d2 == "SAM" or d2 == "MAS"):
                    total = total + 1

    return total
