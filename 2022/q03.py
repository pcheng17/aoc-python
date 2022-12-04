from aocd import data

def getPriority(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1


def partA(dataList):
    result = 0
    for line in dataList:
        firstHalf = set(line[0 : len(line)//2])
        secondHalf = set(line[len(line) // 2:])
        for char in firstHalf.intersection(secondHalf):
            result += getPriority(char)
    return result


def partB(dataList):
    result = 0
    for i in range(0, len(dataList), 3):
        first = set(dataList[i])
        second = set(dataList[i+1])
        third = set(dataList[i+2])
        for char in first.intersection(second, third):
            result += getPriority(char)
    return result

dataList = data.split('\n') 
print(f'Part A: {partA(dataList)}')
print(f'Part B: {partB(dataList)}')

