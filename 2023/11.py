from common.utils import manhattan
from common.grid import Grid2D

from itertools import combinations

def solve(grid, expansion):
    galaxies = grid.find_all('#')
    empty_rows = set(range(grid.rows())) - set(i for i, _ in galaxies)
    empty_cols = set(range(grid.cols())) - set(j for _, j in galaxies)
    
    total = 0
    for g1, g2 in combinations(galaxies, 2):
        total += manhattan(g1, g2) 

        x1, x2 = min(g1[0], g2[0]), max(g1[0], g2[0])
        y1, y2 = min(g1[1], g2[1]), max(g1[1], g2[1]) 

        drows = sum(int(x1 < r < x2) for r in empty_rows)
        dcols = sum(int(y1 < c < y2) for c in empty_cols) 
        
        total += (expansion - 1) * drows
        total += (expansion - 1) * dcols

    return total

def part_a(input):
    return solve(Grid2D(input), 2)

def part_b(input):
    return solve(Grid2D(input), 1000000)
