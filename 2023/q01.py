from aocd import data

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(data):
    return data.splitlines()

def partA(input):
    pass

def partB(input):
    pass

def solveA(input):
    return partA(input)

def solveB(input):
    return partB(input)

if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
