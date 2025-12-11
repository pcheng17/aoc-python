def solve(graph, start, end):
    paths = {x : 0 for x in graph}
    visited = set()

    def dfs(node, end):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor == end:
                paths[node] += 1
                continue

            if neighbor not in visited:
                dfs(neighbor, end)

            paths[node] += paths[neighbor]

    dfs(start, end)
    return paths[start]

def part_a(input):
    graph = {}
    for row in input.splitlines():
        a, b = row.split(': ')
        graph[a] = [c.strip() for c in b.split(' ')]
    return solve(graph, 'you', 'out')

def part_b(input):
    graph = {}
    for row in input.splitlines():
        a, b = row.split(': ')
        graph[a] = [c.strip() for c in b.split(' ')]
    graph['out'] = []

    a = solve(graph, 'svr', 'fft') * solve(graph, 'fft', 'dac') * solve(graph, 'dac', 'out')
    b = solve(graph, 'svr', 'dac') * solve(graph, 'dac', 'fft') * solve(graph, 'fft', 'out')
    return a + b
