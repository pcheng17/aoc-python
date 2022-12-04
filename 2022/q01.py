from aocd import data


def findTotalCalories(inputList):
    calories = []
    for line in inputList:
        calories.append(sum(map(int, line.split())))
    return calories

def partA(inputList):
    cals = findTotalCalories(inputList)
    return max(cals)

def partB(inputList):
    cals = sorted(findTotalCalories(inputList))
    return cals[-3] + cals[-2] + cals[-1]


inputList = data.split('\n\n')
print(f"Part A: {partA(inputList)}")
print(f"Part B: {partB(inputList)}")

