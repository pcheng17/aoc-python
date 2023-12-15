import curses
import time

def t(grid):
    '''Tranpose the grid of strings into a new grid of strings'''
    return list(map(''.join, zip(*grid)))

def sw_step(grid):
    return [row.replace('.O', 'O.') for row in grid]

def se_step(grid):
    return [row.replace('O.', '.O') for row in grid]

def score(grid):
    return sum((len(grid) - i) * (c == 'O') for i, row in enumerate(grid) for c in row)

def advance_frame(grid, dir):
    if dir == 'N':
        return t(sw_step(t(grid)))
    elif dir == 'E':
        return se_step(grid)
    elif dir == 'S':
        return t(se_step(t(grid)))
    elif dir == 'W':
        return sw_step(grid)

def draw_frame(win, grid, cycle, score):
    win.clear()
    max_y, max_x = win.getmaxyx()
    y, x = 0, 0  # Starting coordinates (top-left corner of the window)
    for idx, row in enumerate(grid):
        start_x = (max_x - len(row)) // 2
        start_y = (max_y - len(grid)) // 2 + idx
        win.addstr(start_y, start_x, row)
    # win.addstr(start_y + 2, start_x - 5, f'Cycle: {cycle}, Score: {score}')
    win.refresh()

def main(stdscr):
    # Disable color functionality
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    # Hide cursor
    curses.curs_set(0)

    with open(f'./2023/examples/14.txt', 'r') as f:
        data = f.read()
        if len(data) == 0:
            raise ValueError('Example file is empty')

    grid = data.splitlines()

    for c in range(1, 1000000):
        s = score(grid)
        for d in 'NWSE':
            while True:
                draw_frame(stdscr, grid, c, s)
                time.sleep(0.12)  # Wait for half a second
                grid_new = advance_frame(grid, d)
                if grid == grid_new:
                    break
                grid = grid_new 

curses.wrapper(main)
