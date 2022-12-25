from aocd import data
import math


test = '''
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
'''

CONV = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}


def toBase5(num):
    s = ""
    while num:
        s = str(num % 5) + s
        num //= 5
    return s


def fromSNAFU(numStr: str):
    result = 0
    for i, c in enumerate(numStr[::-1]):
        result += CONV[c] * math.pow(5, i)
    return result


def toSNAFU(num: int):
    digits = list(toBase5(num))
    digits = digits[::-1]
    for i in range(len(digits)-1):
        if digits[i] == '3':
            digits[i+1] = str(int(digits[i+1]) + 1)
            digits[i] = '='
        elif digits[i] == '4':
            digits[i+1] = str(int(digits[i+1]) + 1)
            digits[i] = '-'
        elif digits[i] == '5':
            digits[i+1] = str(int(digits[i+1]) + 1)
            digits[i] = '0'
    return ''.join(digits[::-1])


def parse(data):
    return [line for line in data.strip().splitlines()]


def partA(input):
    total = sum([fromSNAFU(x) for x in input])
    return toSNAFU(int(total))


def partB(input):
    pass


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
