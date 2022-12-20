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
    # oroc = Ore Robot Ore Cost
    # croc = Clay Robot Ore Cost
    # obroc = OBsidian Robot Ore Cost
    # obrcc = OBsidian Robot Clay Cost
    # groc = Geode Robot Ore Cost
    # grobc = Geode Robot OBsidian Cost
    bp_idx, oroc, croc, obroc, obrcc, groc, grobc = blueprint

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

    # while queue:
    #     state = queue.popleft()
    #     orr, cr, obr, gr, oc, cc, obc, gc, tr = state
    #
    #     if state in seen:
    #         continue


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
