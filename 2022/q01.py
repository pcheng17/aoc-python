from aocd import get_data
from common.utils import nlargest

raw_data = get_data(day=1, year=2022)

def parse(data):
    return data.split('\n\n')

def findTotalCalories(inputList):
    return [sum(map(int, line.split())) for line in inputList]

def part_a(inputList):
    return max(findTotalCalories(inputList))

def part_b(inputList):
    return sum(nlargest(3, findTotalCalories(inputList)))
