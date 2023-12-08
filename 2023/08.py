from itertools import cycle
import math

def part_a(input):
    data = input.splitlines()
    dirs = data[0]
    dirs = dirs.translate(str.maketrans('LR', '01'))
    dirs = [int(c) for c in dirs]
    nodes = data[2:]
    network = {}
    for n in nodes:
        a, b = n.split(' = ')
        l, r = b.split(', ')
        network[a] = (l.lstrip('('), r.rstrip(')'))
   
    curr = 'AAA' 
    for i, d in enumerate(cycle(dirs), 1):
        curr = network[curr][d]
        if curr == 'ZZZ':
            return i

def part_b(input):
    data = input.splitlines()
    dirs = data[0]
    dirs = dirs.translate(str.maketrans('LR', '01'))
    dirs = [int(c) for c in dirs]
    nodes = data[2:]
    network = {}
    for n in nodes:
        a, b = n.split(' = ')
        l, r = b.split(', ')
        network[a] = (l.lstrip('('), r.rstrip(')'))

    curr = set(k for k in network.keys() if k.endswith('A'))
    periods = []
    for c in curr:
        for i, d in enumerate(cycle(dirs), 1):
            c = network[c][d]
            if c.endswith('Z'):
                periods.append(i)
                break
    
    return math.lcm(*periods)
