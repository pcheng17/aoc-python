from collections import deque
from aocd import data
import re
import json


test = '''
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
'''



def parse(data):
    blueprints = []
    for line in data.strip().splitlines():
        bp, o, c, o1, o2, g1, g2 = map(int, re.findall('[0-9]+', line))
        blueprints.append((bp, o, c, o1, o2, g1, g2))
    return blueprints


def collect(resources, robots):
    for k, v in robots.items():
        resources[k] += v
    return resources

def buyOreRobot(blueprint, resources, robots):
    resources['ore'] -= blueprint[1]
    robots['ore'] += 1
    return (resources, robots)

def buyClayRobot(blueprint, resources, robots):
    resources['ore'] -= blueprint[2]
    robots['clay'] += 1
    return (resources, robots)

def buyObsidianRobot(blueprint, resources, robots):
    resources['ore'] -= blueprint[3]
    resources['clay'] -= blueprint[4]
    robots['obsidian'] += 1
    return (resources, robots)

def buyGeodeRobot(blueprint, resources, robots):
    resources['ore'] -= blueprint[5]
    resources['obsidian'] -= blueprint[6]
    robots['geode'] += 1
    return (resources, robots)


def dfs(
    blueprint,
    resources,
    robots,
    max_geode_count,
    time_remaining,
    visited,
    dp):

    fset = frozenset(visited)
    dp[fset] = max(dp.get(fset, 0), max_geode_count)

    if time_remaining <= 0:
        return

    print(f'Resources: {resources} ::: Robots: {robots}')

    max_ore_cost = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])

    if resources['ore'] >= blueprint[5] and resources['obsidian'] >= blueprint[6]: 
        # Buy geode robot
        resources = collect(resources, robots)
        resources, robots = buyGeodeRobot(blueprint, resources, robots)
        max_geode_count = resources['geode']
        next_visited = visited.copy()
        next_visited.add((
            json.dumps(resources, sort_keys=True),
            json.dumps(robots, sort_keys=True),
            max_geode_count,
            time_remaining - 1)) 
        dfs(blueprint, resources, robots, max_geode_count, time_remaining - 1, next_visited, dp)

    elif robots['obsidian'] < blueprint[6] and resources['ore'] >= blueprint[3] and resources['clay'] >= blueprint[4]:
        # Buy obsidian robot
        resources = collect(resources, robots)
        resources, robots = buyObsidianRobot(blueprint, resources, robots)
        max_geode_count = resources['geode']
        next_visited = visited.copy()
        next_visited.add((
            json.dumps(resources, sort_keys=True),
            json.dumps(robots, sort_keys=True),
            max_geode_count,
            time_remaining - 1)) 
        dfs(blueprint, resources, robots, max_geode_count, time_remaining - 1, next_visited, dp)

    elif robots['clay'] < blueprint[4] and resources['ore'] >= blueprint[2]:
        # Buy clay robot
        resources = collect(resources, robots)
        resources, robots = buyClayRobot(blueprint, resources, robots)
        max_geode_count = resources['geode']
        next_visited = visited.copy()
        next_visited.add((
            json.dumps(resources, sort_keys=True),
            json.dumps(robots, sort_keys=True),
            max_geode_count,
            time_remaining - 1)) 
        dfs(blueprint, resources, robots, max_geode_count, time_remaining - 1, next_visited, dp)

    elif robots['ore'] < max_ore_cost and resources['ore'] >= blueprint[1]:
        # Buy ore robot
        resources = collect(resources, robots)
        resources, robots = buyOreRobot(blueprint, resources, robots)
        max_geode_count = resources['geode']
        next_visited = visited.copy()
        next_visited.add((
            json.dumps(resources, sort_keys=True),
            json.dumps(robots, sort_keys=True),
            max_geode_count,
            time_remaining - 1)) 
        dfs(blueprint, resources, robots, max_geode_count, time_remaining - 1, next_visited, dp)

    else:
        # Do nothing
        resources = collect(resources, robots)
        max_geode_count = resources['geode']
        next_visited = visited.copy()
        next_visited.add((
            json.dumps(resources, sort_keys=True),
            json.dumps(robots, sort_keys=True),
            max_geode_count,
            time_remaining - 1)) 
        dfs(blueprint, resources, robots, max_geode_count, time_remaining - 1, next_visited, dp)


def simulate(blueprint, total_time) -> int:

    resources = { 'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0 }
    robots    = { 'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0 }

    dp, visited = {}, set()
    max_geode_count = 0
    visited.add((
        resources['ore'], 
        resources['clay'], 
        resources['obsidian'], 
        resources['geode'], 
        robots['ore'], 
        robots['clay'], 
        robots['obsidian'], 
        robots['geode'],
        max_geode_count,
        total_time)) 
    dfs(blueprint, resources, robots, max_geode_count, total_time, visited, dp)
    return max_geode_count


def partA(blueprints):
    return sum((i+1) * simulate(bp, 24) for i, bp in enumerate(blueprints))


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
