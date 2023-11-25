from operator import mul
from functools import reduce
from aocd import get_data
data = get_data(day=3, year=2020)

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(data):
    return data.splitlines()

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

def partA(input):
    return traverse(input, 3, 1)

def partB(input):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(mul, [traverse(input, r, d) for r, d in slopes], 1)

def solveA(input):
    return partA(input)

def solveB(input):
    return partB(input)

if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
