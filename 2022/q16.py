from aocd import data
import re

test='''
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''

def parse(data):
    map = {}
    for line in data.strip().split('\n'):
        src, *dst = re.findall('[A-Z][A-Z]', line)
        flow = int(re.findall('[0-9]+', line)[0])
        map[src] = {'goto': dst, 'flow': flow}
    return map


def partA(input):

    def dfs(curr, time, seen):
        if time <= 1:
            return 0
        flow = 0
        for goto in input[curr]['goto']:
            flow = max(flow, dfs(goto, time-1, seen))
        if curr not in seen and input[curr]['flow'] > 0:
            seen.add(curr)
            flow += input[curr]['flow'] * (time-1)
        
        return flow

    print(dfs('AA', 30, set()))



def partB(input):
    pass


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {partA(input)}')
    # print(f'Part B: {partB(input)}')
