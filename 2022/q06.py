from aocd import data


def parse(data):
    return data

def allUnique(str):
    return len(set(str)) == len(str)

def findFirstUniqueWindow(input, size):
    window = [c for c in input[0:size]]
    if allUnique(window):
        return size
    else:
        for i in range(size, len(input)):
            window.pop(0)
            window.append(input[i])
            if allUnique(window):
                return i+1

def partA(input):
    return findFirstUniqueWindow(input, 4)

def partB(input):
    return findFirstUniqueWindow(input, 14)


input = parse(data)
print(f'Part A: {partA(input)}')
print(f'Part B: {partB(input)}')
