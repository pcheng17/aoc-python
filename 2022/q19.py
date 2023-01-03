from aocd import data
from functools import reduce
import multiprocessing
import re


test = '''
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
'''

global MAX_GEODES
MAX_GEODES = 0


def parse(data):
    blueprints = []
    for line in data.strip().splitlines():
        bp, o, c, o1, o2, g1, g2 = map(int, re.findall('[0-9]+', line))
        blueprints.append((bp, o, c, o1, o2, g1, g2))
    return blueprints

def init_global(x):
    global MAX_GEODES
    MAX_GEODES = x

def dfs(blueprint, ore_count, clay_count, obs_count, geode_count, ore_robot, clay_robot, obs_robot, geode_robot, time_remaining):
    global MAX_GEODES

    MAX_GEODES = max(MAX_GEODES, geode_count)

    if time_remaining <= 1:
        MAX_GEODES = max(MAX_GEODES, geode_count + time_remaining * geode_robot)
        return

    # If MAX_GEODES is greater than the number of geodes we can produce assuming we just
    # keep buying geode robots until the end of time, then stop this branch.
    tmp = time_remaining * (time_remaining - 1) // 2
    if MAX_GEODES >= geode_count + time_remaining * geode_robot + tmp:
        return

    # If we have enough robots to generate resources for a geode robot...
    if ore_robot >= blueprint[5] and obs_robot >= blueprint[6]:
        # If we have enough resources to buy a geode robot...
        if ore_count >= blueprint[5] and obs_count >= blueprint[6]:
            # Buy geode robots until the end of time.
            # But we can easily calculate the ending number of geodes, so let's just do that.
            tmp = time_remaining + (time_remaining - 1) // 2
            MAX_GEODES = max(MAX_GEODES, geode_count + time_remaining * geode_robot + tmp)
        else:
            # Wait a turn because next turn, we'll be ready to easy out
            ore_count += ore_robot
            clay_count += clay_robot
            obs_count += obs_robot
            geode_count += geode_robot
            time_remaining -= 1

            # Easy out
            tmp = time_remaining + (time_remaining - 1) // 2
            MAX_GEODES = max(MAX_GEODES, geode_count + time_remaining * geode_robot + tmp)
        return

    if ore_count >= blueprint[5] and obs_count >= blueprint[6]: 
        # Buy geode robot
        dfs(
            blueprint,
            ore_count + ore_robot - blueprint[5],
            clay_count + clay_robot,
            obs_count + obs_robot - blueprint[6],
            geode_count + geode_robot,
            ore_robot,
            clay_robot,
            obs_robot,
            geode_robot + 1,
            time_remaining - 1
        )
        return

    if obs_robot < blueprint[6] and ore_count >= blueprint[3] and clay_count >= blueprint[4]:
        # Buy obsidian robot
        dfs(
            blueprint,
            ore_count + ore_robot - blueprint[3],
            clay_count + clay_robot - blueprint[4],
            obs_count + obs_robot,
            geode_count + geode_robot,
            ore_robot,
            clay_robot,
            obs_robot + 1,
            geode_robot,
            time_remaining - 1
        )

    max_ore_cost = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
    if ore_robot < max_ore_cost and ore_count >= blueprint[1]:
        # Buy ore robot
        dfs(
            blueprint,
            ore_count + ore_robot - blueprint[1],
            clay_count + clay_robot,
            obs_count + obs_robot,
            geode_count + geode_robot,
            ore_robot + 1,
            clay_robot,
            obs_robot,
            geode_robot,
            time_remaining - 1
        )

    if clay_robot < blueprint[4] and ore_count >= blueprint[2]:
        # Buy clay robot
        dfs(
            blueprint,
            ore_count + ore_robot - blueprint[2],
            clay_count + clay_robot,
            obs_count + obs_robot,
            geode_count + geode_robot,
            ore_robot,
            clay_robot + 1,
            obs_robot,
            geode_robot,
            time_remaining - 1
        )

    # Do nothing
    dfs(
        blueprint,
        ore_count + ore_robot,
        clay_count + clay_robot,
        obs_count + obs_robot,
        geode_count + geode_robot,
        ore_robot,
        clay_robot,
        obs_robot,
        geode_robot,
        time_remaining - 1
    )


def simulate(blueprint, total_time) -> int:
    global MAX_GEODES
    MAX_GEODES = 0

    ore_count, clay_count, obs_count, geode_count = 0, 0, 0, 0
    ore_robot, clay_robot, obs_robot, geode_robot = 1, 0, 0, 0

    dfs(blueprint, ore_count, clay_count, obs_count, geode_count, ore_robot, clay_robot, obs_robot, geode_robot, total_time)
    return MAX_GEODES


def partA(blueprints):
    with multiprocessing.Pool(initializer=init_global, initargs=(0,)) as pool:
        result = pool.starmap(simulate, [(bp, 24) for bp in blueprints])
    return sum((i+1) * r for i, r in enumerate(result))


def partB(blueprints):
    with multiprocessing.Pool(initializer=init_global, initargs=(0,)) as pool:
        result = pool.starmap(simulate, [(bp, 32) for bp in blueprints[0:3]])
    return reduce((lambda x, y: x * y), result)


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
