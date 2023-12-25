from common.utils import nlargest

def findTotalCalories(inputList):
    return [sum(map(int, line.split())) for line in inputList]

def part_a(input):
    return max(findTotalCalories(input.split('\n\n')))

def part_b(input):
    return sum(nlargest(3, findTotalCalories(input.split('\n\n'))))
