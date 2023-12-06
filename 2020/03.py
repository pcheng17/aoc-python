from operator import mul
from functools import reduce
from aocd import get_data

def get_input():
    return get_data(day=3, year=2020)

def parse(input):
    pass

def traverse(input, right, down):
    num_cols = len(input[0])
    trees = 0
    row = 0
    col = 0
    for row in range(0, len(input), down):
        if input[row][col] == '#':
            trees += 1
        col = (col + right) % num_cols
    return trees

def part_a(input):
    return traverse(input.splitlines(), 3, 1)

def part_b(input):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(mul, [traverse(input.splitlines(), r, d) for r, d in slopes], 1)
