from aocd import data
from numpy import inf
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


def dfs(valves, curr, distMap, timeRemaining, visited, flow, dp):
    fset = frozenset(visited)
    dp[fset] = max(dp.get(fset, 0), flow)
    for next in valves:
        if next == curr:
            continue
        # It will take distMap[curr][valve] minutes to get there, and then 1 minute
        # to open the valve.
        minutes = timeRemaining - distMap[curr][next] - 1
        if (next in visited) or (minutes <= 0):
            continue
        else:
            nextVisited = visited.copy()
            nextVisited.add(next)
            dfs(valves, next, distMap, minutes, nextVisited, flow + (minutes * valves[next]), dp)


def floydMarshall(input):
    distMap = {x : {y : 1 if y in input[x]['goto'] else inf for y in input} for x in input}
    for k in distMap:
        for i in distMap:
            for j in distMap:
                distMap[i][j] = min(distMap[i][j], distMap[i][k] + distMap[k][j])
    return distMap


def partA(input, minutes):
    relevantValves = {k : v['flow'] for k, v in input.items() if v['flow'] > 0}

    distMap = floydMarshall(input)

    dp, visited = {}, set()
    dfs(relevantValves, 'AA', distMap, minutes, visited, 0, dp)
    return max(dp.values())


def partB(input, minutes):
    relevantValves = {k : v['flow'] for k, v in input.items() if v['flow'] > 0}

    distMap = floydMarshall(input)

    dp, visited = {}, set()
    dfs(relevantValves, 'AA', distMap, minutes, visited, 0, dp)

    maxFlow = 0
    for myK, myFlow in dp.items():
        for eleK, eleFlow in dp.items():
            if len(myK.intersection(eleK)) == 0:
                maxFlow = max(maxFlow, myFlow + eleFlow)
    
    return maxFlow


def solveA(input):
    return partA(input, 30)


def solveB(input):
    return partB(input, 26)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
