from collections import deque
from aocd import data
import re


def parse(data):
    blueprints = []
    for line in data.splitlines():
        bp, o, c, o1, o2, g1, g2 = map(int, re.findall('[0-9]+', line))
        blueprints.append((bp, o, c, o1, o2, g1, g2))
    return blueprints


def simulate(blueprint, total_time):
    bp_idx, ore_ore, clay_ore, obo_ore, obo_clay, geo_ore, geo_obo = blueprint
    
    max_ore_cost = max(ore_ore, clay_ore, obo_ore, geo_ore)


    # Initial state of the simulation
    #   - Ore robots
    #   - Clay robots
    #   - Obsidian robots
    #   - Geode robots
    #   - Ore count
    #   - Clay count
    #   - Obsidian count
    #   - Geode count
    #   - Time remaining
    initial = (1, 0, 0, 0, 0, 0, 0, 0, total_time)

    queue = deque([initial])
    seen = set()
    max_geodes = 0



def partA(input):



def partB(input):
    pass


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input)


if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
