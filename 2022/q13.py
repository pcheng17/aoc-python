from aocd import data
import json 


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
        pairList.append((json.loads(a), json.loads(b)))
    return pairList


def isInt(x):
    return isinstance(x, int)


def isList(x):
    return isinstance(x, list)


def compare(arg1, arg2):
    if isList(arg1) and isList(arg2):
        for a, b in zip(arg1, arg2):
            tmp = compare(a, b)
            if tmp is not None: return tmp
        return compare(len(arg1), len(arg2))
    elif isList(arg1) and isInt(arg2):
        return compare(arg1, [arg2])
    elif isInt(arg1) and isList(arg2):
        return compare([arg1], arg2)
    else:
        if arg1 == arg2:
            return None
        else:
            return arg1 < arg2


def partA(pairList):
    sum = 0
    for idx, pair in enumerate(pairList):
        if compare(pair[0], pair[1]):
            sum += (idx+1)
    return sum


def partB(allList):
    pos1 = 1 + sum(1 for x in allList if compare(x, [[2]]))
    pos2 = 2 + sum(1 for x in allList if compare(x, [[6]]))
    return pos1 * pos2


if __name__ == '__main__':
    pairList = parse(data)
    print(f'Part A: {partA(pairList)}')

    allList = []
    for a, b in pairList:
        allList.append(a)
        allList.append(b)
    print(f'Part B: {partB(allList)}')
