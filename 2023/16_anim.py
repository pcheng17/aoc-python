import curses
import time

def advance(n):
    if n[2] == '^':
        return (n[0]-1, n[1], '^')
    elif n[2] == '>':
        return (n[0], n[1]+1, '>')
    elif n[2] == 'V':
        return (n[0]+1, n[1], 'V')
    else:
        return (n[0], n[1]-1, '<')

def advance_frame(data, frontier, visited):
    rows = len(data)
    cols = len(data[0])

    next_frontier = []
    for i, j, d in frontier:
        if data[i][j] == '.':
            next_frontier.append(advance((i, j, d)))
        elif data[i][j] == '|':
            if d == '>' or d == '<':
                next_frontier.append((i+1, j, 'V'))
                next_frontier.append((i-1, j, '^'))
            elif d == 'V':
                next_frontier.append((i+1, j, 'V'))
            else:
                next_frontier.append((i-1, j, '^'))
        elif data[i][j] == '-':
            if d == 'V' or d == '^':
                next_frontier.append((i, j+1, '>'))
                next_frontier.append((i, j-1, '<'))
            elif d == '>':
                next_frontier.append((i, j+1, '>'))
            else:
                next_frontier.append((i, j-1, '<'))
        elif data[i][j] == '\\':
            if d == '>':
                next_frontier.append((i+1, j, 'V'))
            elif d == 'V':
                next_frontier.append((i, j+1, '>'))
            elif d == '<':
                next_frontier.append((i-1, j, '^'))
            else:
                next_frontier.append((i, j-1, '<'))
        else:
            if d == '>':
                next_frontier.append((i-1, j, '^'))
            elif d == 'V':
                next_frontier.append((i, j-1, '<'))
            elif d == '<':
                next_frontier.append((i+1, j, 'V'))
            else:
                next_frontier.append((i, j+1, '>'))
    
    # Filter
    next_frontier = [n for n in next_frontier if 0 <= n[0] < rows]
    next_frontier = [n for n in next_frontier if 0 <= n[1] < cols]
    next_frontier = [n for n in next_frontier if n not in visited]
    
    for n in next_frontier:
        visited.add(n)
    frontier = next_frontier 

    return frontier, visited

def draw_frame(win, data, frontier, visited):
    grid = data.copy()
    grid = [[c for c in row] for row in grid]
    for i, j, d in visited:
        grid[i][j] = '#'
    for i, j, d in frontier:
        grid[i][j] = d
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = ' '
    
    win.clear()
    max_y, max_x = win.getmaxyx()
    y, x = 0, 0  # Starting coordinates (top-left corner of the window)
    for idx, row in enumerate(grid):
        start_x = (max_x - len(row)) // 2
        start_y = (max_y - len(grid)) // 2 + idx
        win.addstr(start_y, start_x, ''.join(row))
    win.refresh()

def main(stdscr):
    # Disable color functionality
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    # Hide cursor
    curses.curs_set(0)

    with open(f'./2023/examples/16_real.txt', 'r') as f:
        data = f.read()
        if len(data) == 0:
            raise ValueError('Example file is empty')

    grid = data.splitlines()

    frontier = [(0, 0, '>')]

    visited = set()
    visited.add((0, 0, '>'))

    while True:
        frontier, visited = advance_frame(grid, frontier, visited)
        if not frontier:
            time.sleep(5)
        draw_frame(stdscr, grid, frontier, visited)
        time.sleep(0.04)

curses.wrapper(main)
