from aocd import data
import re


def parse(data):
    valveMap = {}
    flowMap = {}
    for line in data.strip().split('\n'):
        src, *dst = re.findall('[A-Z][A-Z]', line)
        valveMap[src] = dst
        flowMap[src] = int(re.findall('[0-9]+', line)[0])
    return (valveMap, flowMap)


def partA(valveMap, flowMap):

    flows = [(k,v) for k, v in flowMap.items()]
    flows = sorted(flows, key = lambda x : x[1], reverse=True)


    pass


def partB(input):
    pass


def solveA(input):
    valveMap, flowMap = input
    return partA(valveMap, flowMap)


def solveB(input):
    return partB(input)


# if __name__ == '__main__':
#     input = parse(data)
#     print(f'Part A: {partA(input)}')
#     print(f'Part B: {partB(input)}')
