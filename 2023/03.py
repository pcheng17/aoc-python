from aocd import get_data
from math import prod
from collections import defaultdict
import re

# raw_data = '467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..\n'

def get_input():
    return get_data(day=3, year=2023)

def is_symbol(c):
    return (not c.isdigit() and c != '.')

def is_star(c):
    return c == '*'

def part_a(input):
    data = input.splitlines()
    rows = len(data)
    cols = len(data[0])

    numbers = []
    for i, line in enumerate(data):
        match = re.finditer(r'([0-9]+)', line)
        for m in match:
            numbers.append((i, m.span(), m.group()))

    total = 0
    for idx, n in enumerate(numbers):
        included = False
        for ii in range(n[0]-1, n[0]+2):
            for jj in range(n[1][0]-1, n[1][1]+1):
                if 0 <= ii < rows and 0 <= jj < cols:
                    if is_symbol(data[ii][jj]):
                        total += int(n[2])
                        included = True
                        break
            if included:
                break
    
    return total

def part_b(input):
    data = input.splitlines() 
    rows = len(data)
    cols = len(data[0])

    numbers = []
    for i, line in enumerate(data):
        match = re.finditer(r'([0-9]+)', line)
        for m in match:
            numbers.append((i, m.span(), m.group()))

    gear_neighbors = defaultdict(list) 
    for idx, n in enumerate(numbers):
        for ii in range(n[0]-1, n[0]+2):
            for jj in range(n[1][0]-1, n[1][1]+1):
                if 0 <= ii < rows and 0 <= jj < cols:
                    if is_star(data[ii][jj]):
                        gear_neighbors[(ii, jj)].append(int(n[2]))
    
    return sum(prod(v) for v in gear_neighbors.values() if len(v) == 2)
