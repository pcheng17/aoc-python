from itertools import combinations
from collections import defaultdict
from graphviz import Graph
import re

def part_a(input):
    data = input.split('\n')
    graph = defaultdict(set)
    nodes = set()
    for row in data:
        lhs, rhs = row.split(': ')
        rhs = rhs.split(' ')
        graph[lhs].update(rhs)
        nodes.add(lhs)
        nodes.update(rhs)

    # dot = Graph()
    # for k, v in graph.items():
    #     for vv in v:
    #         dot.edge(k, vv)

    # with open('25.dot', 'w') as f:
    #     f.write(dot.source)

    bound = 27450
    with open('./2023/25.svg', 'r') as f:
        data = f.read()
    data = data.splitlines()
    rows = [row for row in data if row.startswith('<text')]
    xs = [int(re.search(r'x="([^"]*)"', row).group(1)) for row in rows]
    left = sum(int(x < bound) for x in xs)
    return left * (len(rows) - left)

def part_b(input):
    return 'Done!'
