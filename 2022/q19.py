from collections import deque
from aocd import data
import re


test = '''
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
'''

def parse(data):
    blueprints = []
    for line in data.strip().splitlines():
        bp, o, c, o1, o2, g1, g2 = map(int, re.findall('[0-9]+', line))
        blueprints.append((bp, o, c, o1, o2, g1, g2))
    return blueprints


def dfs(
    blueprint,
    ore_robots,
    clay_robots,
    obsidian_robots,
    geode_robots,
    ore_count,
    clay_count,
    obsidian_count,
    geode_count,
    time_remaining):

    idx, oroc, croc, obroc, obrcc, groc, grobc = blueprint

    max_ore_cost = max(oroc, croc, obroc, groc)

    if ore_robots < max_ore_cost and ore_count >= oroc:
        # Buy ore robot
        dfs(
            blueprint, 
            ore_robots+1, 
            clay_robots, 
            obsidian_robots, 
            geode_robots, 
            ore_count + ore_robots - oroc, 
            clay_count + clay_robots, 
            obsidian_count + obsidian_robots, 
            geode_count + geode_robots, 
            time_remaining - 1)
    elif clay_robots < obrcc and ore_count >= croc:
        # Buy clay robot
        dfs(
            blueprint,
            ore_robots,
            clay_robots + 1,
            obsidian_robots,
            geode_robots,
            ore_count + ore_robots - croc,
            clay_count + clay_robots,
            obsidian_count + obsidian_robots,
            geode_count + geode_robots,
            time_remaining - 1)
    else:
        # Do nothing
        dfs(
            blueprint,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
            ore_count + ore_robots,
            clay_count + clay_robots,
            obsidian_count + obsidian_robots,
            geode_count + geode_robots,
            time_remaining - 1)





def simulate(blueprint, total_time) -> int:
    # oroc = Ore Robot Ore Cost
    # croc = Clay Robot Ore Cost
    # obroc = OBsidian Robot Ore Cost
    # obrcc = OBsidian Robot Clay Cost
    # groc = Geode Robot Ore Cost
    # grobc = Geode Robot OBsidian Cost
    idx, oroc, croc, obroc, obrcc, groc, grobc = blueprint

    max_ore_cost = max(oroc, croc, obroc, groc)

    # Initial state of the simulation
    #   0) Ore robots
    #   1) Clay robots
    #   2) Obsidian robots
    #   3) Geode robots
    #   4) Ore count
    #   5) Clay count
    #   6) Obsidian count
    #   7) Geode count
    #   8) Time remaining
    initial = (1, 0, 0, 0, 0, 0, 0, 0, total_time)

    queue = deque([initial])
    seen = set()
    max_geodes = 0

    while queue:
        state = queue.popleft()
        orr, cr, obr, gr, oc, cc, obc, gc, tr = state

        if gc > max_geodes:
            max_geodes = gc

        # Stopping condition on time
        if tr == 0:
            break

        if orr < max_ore_cost and oc >= oroc:
            queue.append((orr+1, cr, obr, gr, oc+orr-oroc, cc+cr, obc+obr, gc+gr, tr-1))
        elif cr < obrcc and oc >= croc: 
            queue.append((orr, cr+1, obr, gr, oc+orr-croc, cc+cr, obc+obr, gc+gr, tr-1))
        else:
            queue.append((orr, cr, obr, gr, oc+orr, cc+cr, obc+obc, gc+gr, tr-1))

        print(queue)

    return max_geodes



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
