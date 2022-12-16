from aocd import data
from common.utils import nlargest

def parse(data):
    return data.split('\n\n')

def findTotalCalories(inputList):
    return [sum(map(int, line.split())) for line in inputList]

def partA(inputList):
    return max(findTotalCalories(inputList))

def partB(inputList):
    return sum(nlargest(3, findTotalCalories(inputList)))

def solveA(input):
    return partA(input)

def solveB(input):
    return partB(input)

if __name__ == '__main__':
    input = parse(data)
    print(f"Part A: {partA(input)}")
    print(f"Part B: {partB(input)}")
