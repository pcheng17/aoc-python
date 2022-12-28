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


def dfs(blueprint, ore_count, clay_count, obs_count, geode_count, ore_robot, clay_robot, obs_robot, geode_robot, max_geode_count, time_remaining, visited, dp):

    fset = frozenset(visited)
    dp[fset] = max(dp.get(fset, 0), max_geode_count)

    if time_remaining <= 0:
        return
    
    print(ore_count, clay_count, obs_count, geode_count, ore_robot, clay_robot, obs_robot, geode_robot, max_geode_count, time_remaining)

    max_ore_cost = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])

    if ore_count >= blueprint[5] and obs_count >= blueprint[6]: 
        # Buy geode robot
        state = (
            ore_count + ore_robot - blueprint[5],
            clay_count + clay_robot,
            obs_count + obs_robot - blueprint[6],
            geode_count + geode_robot,
            ore_robot,
            clay_robot,
            obs_robot,
            geode_robot + 1,
            max_geode_count + geode_robot,
            time_remaining - 1
        )
        if state not in visited:
            next_visited = visited.copy()
            next_visited.add(state)
            dfs(blueprint, *state, next_visited, dp)

    if obs_robot < blueprint[6] and ore_count >= blueprint[3] and clay_count >= blueprint[4]:
        # Buy obsidian robot
        state = (
            ore_count + ore_robot - blueprint[3],
            clay_count + clay_robot - blueprint[4],
            obs_count + obs_robot,
            geode_count + geode_robot,
            ore_robot,
            clay_robot,
            obs_robot + 1,
            geode_robot,
            max_geode_count + geode_robot,
            time_remaining - 1
        )
        if state not in visited:
            next_visited = visited.copy()
            next_visited.add(state)
            dfs(blueprint, *state, next_visited, dp)

    if clay_robot < blueprint[4] and ore_count >= blueprint[2]:
        # Buy clay robot
        state = (
            ore_count + ore_robot - blueprint[2],
            clay_count + clay_robot,
            obs_count + obs_robot,
            geode_count + geode_robot,
            ore_robot,
            clay_robot + 1,
            obs_robot,
            geode_robot,
            max_geode_count + geode_robot,
            time_remaining - 1
        )
        if state not in visited:
            next_visited = visited.copy()
            next_visited.add(state)
            dfs(blueprint, *state, next_visited, dp)

    if ore_robot < max_ore_cost and ore_count >= blueprint[1]:
        # Buy ore robot
        state = (
            ore_count + ore_robot - blueprint[1],
            clay_count + clay_robot,
            obs_count + obs_robot,
            geode_count + geode_robot,
            ore_robot + 1,
            clay_robot,
            obs_robot,
            geode_robot,
            max_geode_count + geode_robot,
            time_remaining - 1
        )
        if state not in visited:
            next_visited = visited.copy()
            next_visited.add(state)
            dfs(blueprint, *state, next_visited, dp)

    # Do nothing
    state = (
        ore_count + ore_robot,
        clay_count + clay_robot,
        obs_count + obs_robot,
        geode_count + geode_robot,
        ore_robot,
        clay_robot,
        obs_robot,
        geode_robot,
        max_geode_count + geode_robot,
        time_remaining - 1
    )
    if state not in visited:
        next_visited = visited.copy()
        next_visited.add(state)
        dfs(blueprint, *state, next_visited, dp)


def simulate(blueprint, total_time) -> int:

    ore_count, clay_count, obs_count, geode_count = 0, 0, 0, 0
    ore_robot, clay_robot, obs_robot, geode_robot = 1, 0, 0, 0

    dp, visited = {}, set()
    max_geode_count = 0
    visited.add((
        ore_count, clay_count, obs_count, geode_count,
        ore_robot, clay_robot, obs_robot, geode_robot,
        max_geode_count,
        total_time)) 
    dfs(blueprint, ore_count, clay_count, obs_count, geode_count, ore_robot, clay_robot, obs_robot, geode_robot, max_geode_count, total_time, visited, dp)
    return max(dp.values())


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
