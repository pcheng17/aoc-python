from heapq import heapify, heappush, heappop
from collections import defaultdict
from itertools import combinations
import sys

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def is_valid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] != "#"

def is_branch(grid, pos):
    return sum(int(grid[pos[0]+dx][pos[1]+dy] == '.') for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))) > 2

def part_a_dfs(input):
    def dfs(grid, goal, pos, dist, visited):
        if pos == goal:
            return dist

        ghosts = []

        a, b = pos

        if grid[a][b] == ">":
            if is_valid(grid, (a, b + 1)) and (a, b + 1) not in visited:
                visited.add((a, b + 1))
                ghosts.append(dfs(grid, goal, (a, b + 1), dist + 1, visited))
                visited.remove((a, b + 1))
        elif grid[a][b] == "<":
            if is_valid(grid, (a, b - 1)) and (a, b - 1) not in visited:
                visited.add((a, b - 1))
                ghosts.append(dfs(grid, goal, (a, b - 1), dist + 1, visited))
                visited.remove((a, b - 1))
        elif grid[a][b] == "^":
            if is_valid(grid, (a - 1, b)) and (a - 1, b) not in visited:
                visited.add((a - 1, b))
                ghosts.append(dfs(grid, goal, (a - 1, b), dist + 1, visited))
                visited.remove((a - 1, b))
        elif grid[a][b] == "v":
            if is_valid(grid, (a + 1, b)) and (a + 1, b) not in visited:
                visited.add((a + 1, b))
                ghosts.append(dfs(grid, goal, (a + 1, b), dist + 1, visited))
                visited.remove((a + 1, b))
        else:
            for dx, dy in (up, down, left, right):
                an = pos[0] + dx
                bn = pos[1] + dy
                if is_valid(grid, (an, bn)) and (an, bn) not in visited:
                    visited.add((an, bn))
                    ghosts.append(dfs(grid, goal, (an, bn), dist + 1, visited))
                    visited.remove((an, bn))
        return max(ghosts) if ghosts else 0

    sys.setrecursionlimit(1000000)
    grid = input.splitlines()
    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)
    return dfs(grid, end, start, 0, {start})

def part_a_bfs(input):
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

def part_a(input):
    return part_a_dfs(input)

def find_max_distance_on_grid(grid, start, end, avoid):
    def dfs(grid, goal, pos, dist, visited):
        if pos == goal:
            return dist

        ghosts = []

        for dx, dy in (up, down, left, right):
            an = pos[0] + dx
            bn = pos[1] + dy
            if is_valid(grid, (an, bn)) and (an, bn) not in visited and (an, bn) not in avoid:
                visited.add((an, bn))
                ghosts.append(dfs(grid, goal, (an, bn), dist + 1, visited))
                visited.remove((an, bn))
        return max(ghosts) if ghosts else 0

    return dfs(grid, end, start, 0, {start})

def find_max_distance_on_graph(graph, distance_matrix, start, end):
    def dfs(graph, goal, pos, dist, visited):
        if pos == goal:
            return dist
        ghosts = []
        for neighbor in graph[pos]:
            if neighbor not in visited:
                visited.add(neighbor)
                ghosts.append(dfs(graph, goal, neighbor, dist + distance_matrix[(pos, neighbor)], visited))
                visited.remove(neighbor)
        return max(ghosts) if ghosts else 0

    return dfs(graph, end, start, 0, {start})

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
