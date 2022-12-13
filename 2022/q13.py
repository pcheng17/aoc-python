from aocd import data
import numpy as np


# a = [2, 3, 4, 1, 1]
# b = [2, 3, 5, 1, 1]
#
# print(np.lexsort(np.array([a, b]).T))

test = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''


def parse(data):
    pairList = []
    pairsStr = data.split('\n\n')
    for pair in pairsStr:
        a, b = pair.split('\n')
        pairList.append((eval(a), eval(b)))
    return pairList

def compare(arg1, arg2):
    if type(arg1) == list and type(arg2) == list:
        for a, b in zip(arg1, arg2):
            aHasList = any(isinstance(x, list) for x in a)
            bHasList = any(isinstance(x, list) for x in b)
            if not aHasList and not bHasList:
                order = np.lexsort(np.array([a, b]).T)
                return order[0] == 0
            else:
                return compare(a, b)
    elif type(arg1) == list and type(arg2) == int:
        return compare(arg1, [arg2])
    elif type(arg1) == int and type(arg2) == list:
        return compare([arg1], arg2)
    else:
        return compare([arg1], [arg2])



def partA(pairList):
    sum = 0
    for idx, pair in enumerate(pairList):
        if compare(pair[0], pair[1]):
            print(idx+1)
            sum += (idx+1)
    return sum



def partB(input):
   raise NotImplementedError


if __name__ == '__main__':
    pairList = parse(test)
    print(f'Part A: {partA(pairList)}')
    # print(f'Part B: {partB(input)}')
