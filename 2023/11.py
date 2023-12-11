from common.utils import manhattan_dist

def solve(grid, expansion):
    nrows = len(grid)
    ncols = len(grid[0])

    empty_rows = []
    for i, row in enumerate(grid):
        if all(c == '.' for c in row):
            empty_rows.append(i)
        
    empty_cols = []
    for j in range(ncols):
        if all(grid[i][j] == '.' for i in range(nrows)):
            empty_cols.append(j)
    
    galaxies = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == '#':
                galaxies.append((i, j))
    ngalaxies = len(galaxies)
    
    total = 0
    for i in range(ngalaxies):
        for j in range(i+1, ngalaxies):
            g1 = galaxies[i]  
            g2 = galaxies[j]
            dist = manhattan_dist(g1, g2) 

            x1 = min(g1[0], g2[0])
            x2 = max(g1[0], g2[0])
            
            y1 = min(g1[1], g2[1])
            y2 = max(g1[1], g2[1]) 

            drows = sum(int(x1 < r < x2) for r in empty_rows)
            dcols = sum(int(y1 < c < y2) for c in empty_cols) 
            
            dist += (expansion - 1) * drows
            dist += (expansion - 1) * dcols
            total += dist
    return total

def part_a(input):
    grid = [[c for c in line] for line in input.splitlines()]
    return solve(grid, 2)

def part_b(input):
    grid = [[c for c in line] for line in input.splitlines()]
    return solve(grid, 1000000)
