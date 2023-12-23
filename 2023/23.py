from heapq import heapify, heappush, heappop
from collections import defaultdict
from itertools import combinations

def is_valid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] != "#"

def is_branch(grid, pos):
    return sum(int(grid[pos[0]+dx][pos[1]+dy] == '.') for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))) > 2

def part_a(input):
    grid = input.splitlines()

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 1)
    end = (rows - 1, cols - 2)

    queue = [(0, start, set())]
    heapify(queue)

    current_max = 0

    while queue:
        dist, pos, v = heappop(queue)

        if pos == end:
            current_max = min(current_max, dist)
            continue

        v.add(pos)

        pa, pb = pos

        if grid[pa][pb] == ">":
            if (pa, pb + 1) not in v:
                heappush(queue, (dist - 1, (pa, pb + 1), v.copy()))
        elif grid[pa][pb] == "<":
            if (pa, pb - 1) not in v:
                heappush(queue, (dist - 1, (pa, pb - 1), v.copy()))
        elif grid[pa][pb] == "^":
            if (pa - 1, pb) not in v:
                heappush(queue, (dist - 1, (pa - 1, pb), v.copy()))
        elif grid[pa][pb] == "v":
            if (pa + 1, pb) not in v:
                heappush(queue, (dist - 1, (pa + 1, pb), v.copy()))
        elif grid[pa][pb] == ".":
            if is_valid(grid, (pa, pb + 1)) and (pa, pb + 1) not in v:
                heappush(queue, (dist - 1, (pa, pb + 1), v.copy()))
            if is_valid(grid, (pa, pb - 1)) and (pa, pb - 1) not in v:
                heappush(queue, (dist - 1, (pa, pb - 1), v.copy()))
            if is_valid(grid, (pa + 1, pb)) and (pa + 1, pb) not in v:
                heappush(queue, (dist - 1, (pa + 1, pb), v.copy()))
            if is_valid(grid, (pa - 1, pb)) and (pa - 1, pb) not in v:
                heappush(queue, (dist - 1, (pa - 1, pb), v.copy()))

    return -current_max

def find_max_distance_on_grid(grid, start, end, avoid):
    queue = [(0, start, set())]
    heapify(queue)

    current_max = 0

    while queue:
        dist, pos, v = heappop(queue)

        if pos in avoid or pos in v:
            continue

        if pos == end:
            current_max = min(current_max, dist)
            continue

        v.add(pos)

        pa, pb = pos

        if is_valid(grid, (pa, pb + 1)):
            heappush(queue, (dist - 1, (pa, pb + 1), v.copy()))
        if is_valid(grid, (pa, pb - 1)):
            heappush(queue, (dist - 1, (pa, pb - 1), v.copy()))
        if is_valid(grid, (pa + 1, pb)):
            heappush(queue, (dist - 1, (pa + 1, pb), v.copy()))
        if is_valid(grid, (pa - 1, pb)):
            heappush(queue, (dist - 1, (pa - 1, pb), v.copy()))

    return -current_max

def find_max_distance_on_graph(graph, distance_matrix, start, end):
    queue = [(0, start, set())]
    heapify(queue)
    current_max = 0
    while queue:
        dist, pos, v = heappop(queue)
        if pos == end:
            current_max = min(current_max, dist)
            continue
        v.add(pos)
        for neighbor in graph[pos]:
            if neighbor not in v and distance_matrix[(pos, neighbor)] > 0:
                heappush(queue, (dist - distance_matrix[(pos, neighbor)], neighbor, v.copy()))
    return -current_max

def part_b(input):
    grid = input.splitlines()
    for i in range(len(grid)):
        grid[i] = grid[i].translate(str.maketrans("^v<>", "...."))

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 1)
    end = (rows - 1, cols - 2)

    # Find all branch points
    coarse_nodes = set()
    coarse_nodes.add(start)
    coarse_nodes.add(end)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if grid[i][j] == "." and is_branch(grid, (i, j)):
                coarse_nodes.add((i, j))

    distance_matrix = defaultdict(lambda: float("-inf"))

    for a, b in combinations(coarse_nodes, 2):
        d = find_max_distance_on_grid(grid, a, b, [x for x in coarse_nodes if x not in [a, b]])
        distance_matrix[(a, b)] = d
        distance_matrix[(b, a)] = d

    graph = defaultdict(list)
    for a, b in combinations(coarse_nodes, 2):
        if distance_matrix[(a, b)] > 0:
            graph[a].append(b)
            graph[b].append(a)

    return find_max_distance_on_graph(graph, distance_matrix, start, end)
