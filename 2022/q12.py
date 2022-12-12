from aocd import data
import numpy as np

test = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''

DIRS = [
    np.array([1, 0], dtype=int), 
    np.array([-1, 0], dtype=int),
    np.array([0, 1], dtype=int),
    np.array([0, -1], dtype=int)
]

def parse(data):
    grid = []
    for line in data.splitlines():
        grid.append([c for c in line])

    start = None
    finish = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = [i, j]
                grid[i][j] = 'a'
            elif grid[i][j] == 'E':
                finish = [i, j]
                grid[i][j] = 'z';
    
    # Convert grid to numbers so comparisons are easier (in my head)
    grid = [list(map(lambda x : ord(x) - ord('a'), row)) for row in grid]
    return np.array(start, dtype=int), np.array(finish, dtype=int), grid


def partA(start, finish, grid):
    nRows = len(grid)
    nCols = len(grid[0])
    visited = [[False for _ in range(nCols)] for _ in range(nRows)]
    visited[start[0]][start[1]] = True

    queue = [start]
    steps = 0

    while len(queue):
        tmp = []
        for curr in queue:
            if (curr == finish).all():
                return steps
            for dir in DIRS:
                next = curr + dir
                if 0 <= next[0] < nRows and 0 <= next[1] < nCols and not visited[next[0]][next[1]] and grid[next[0]][next[1]] <= grid[curr[0]][curr[1]]+1:
                    tmp.append(next)
                    visited[next[0]][next[1]] = True
        steps += 1
        queue = tmp

    return -1


def partB(finish, grid):
    nRows = len(grid)
    nCols = len(grid[0])
    visited = [[False for _ in range(nCols)] for _ in range(nRows)]
    visited[start[0]][start[1]] = True

    # Find all possible starts
    queue = []
    for i in range(nRows):
        for j in range(nCols):
            if grid[i][j] == 0:
                queue.append(np.array([i,j], dtype=int))

    steps = 0

    while len(queue):
        tmp = []
        for curr in queue:
            if (curr == finish).all():
                return steps
            for dir in DIRS:
                next = curr + dir
                if 0 <= next[0] < nRows and 0 <= next[1] < nCols and not visited[next[0]][next[1]] and grid[next[0]][next[1]] <= grid[curr[0]][curr[1]]+1:
                    tmp.append(next)
                    visited[next[0]][next[1]] = True
        steps += 1
        queue = tmp

    return -1


if __name__ == '__main__':
    start, finish, grid = parse(data)
    print(f'Part A: {partA(start, finish, grid)}')
    print(f'Part B: {partB(finish, grid)}')
