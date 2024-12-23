from collections import defaultdict
from graphviz import Digraph

def part_a(input):
    graph = defaultdict(set)
    dot = Digraph()
    for row in input.splitlines():
        a, b = row.split("-")
        dot.edge(a, b)
        graph[a].add(b)
        graph[b].add(a)

    # Find all 3-cycles
    triangles = set()
    for a in graph:
        for b in graph[a]:
            for c in graph[a]:
                if b != c and c in graph[b]:
                    triangles.add(tuple(sorted([a, b, c])))

    print(f"Found {len(triangles)} triangles")
    return len([tri for tri in triangles if any(x for x in tri if x.startswith('t'))])

def part_b(input):
    graph = defaultdict(set)
    for row in input.splitlines():
        a, b = row.split("-")
        graph[a].add(b)
        graph[b].add(a)

    # Find the largest complete subgraph
    nodes = set(graph.keys())
    curr_best = set()

    while nodes:
        degs = {node: len(graph[node]) for node in nodes}
        curr = max(degs.items(), key=lambda x: x[1])[0]
        subgraph = {curr}
        candidates = set(graph[curr])
        while candidates:
            valid_candidates = {
                v : len(graph[v].intersection(subgraph))
                for v in candidates
                if all(u in graph[v] for u in subgraph)
            }

            if not valid_candidates:
                break

            curr = max(valid_candidates.items(), key=lambda x: x[1])[0]
            subgraph.add(curr)

            candidates = candidates.intersection(graph[curr])

        if curr_best is None or len(subgraph) > len(curr_best):
            curr_best = subgraph

        nodes -= subgraph

    return ','.join(sorted(curr_best))

