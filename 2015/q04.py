from aocd import data
import hashlib

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(data):
    return data.splitlines()

def find_solution(secret_key, prefix):
    num = 0
    while True:
        candidate = f'{secret_key}{num}'
        tmp = hashlib.md5(candidate.encode('utf-8')).hexdigest()
        if tmp.startswith(prefix):
            return num
        num += 1

def partA(input):
    return find_solution(input[0], '00000')

def partB(input):
    return find_solution(input[0], '000000')

def solveA(input):
    return partA(input)

def solveB(input):
    return partB(input)

if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
