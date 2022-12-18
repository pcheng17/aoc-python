import datetime
import importlib
import os
import sys
import time


# TODO Gracefully error out if file doesn't exist
# TODO If the runner received no args, run today's aoc 
# TODO Consider giving myself a way to run test code too?


def main(args):
    part = None
    if len(args) == 2:
        year, day = args
    else:
        year, day, *part = args

    if len(day) == 1: day = '0' + day

    daysTil = 25 - int(day)
    dateStr = datetime.datetime(int(year), 12, int(day)).strftime('%B %d, %Y')
    if daysTil > 0:
        countdownStr = f'{25 - int(day)} day{"" if daysTil == 1 else "s"} til Christmas'
    else:
        countdownStr = 'Merry Christmas!'
    titleStr = f'|        Advent of Code :: {dateStr} :: {countdownStr}       |'
    separator = '+' + '-' * (len(titleStr) - 2) + '+'

    print(separator)
    print(titleStr)
    print(separator)

    if not os.path.exists(f'./{year}/q{day}.py'):
        print(f'Solution code doesn\'t exist.')
        return

    module = importlib.import_module(f'{year}.q{day}')
    input = module.parse(module.data)

    if part is not None:
        t0 = time.time()
        sol = getattr(module, f'solve{part[0]}')(input)
        t1 = time.time()
        print(f'🎄 Part {part[0]}: {sol} :: {t1-t0:.6f} sec')
    else:
        for x in ['A', 'B']:
            t0 = time.time()
            sol = getattr(module, f'solve{x}')(input)
            t1 = time.time()
            print(f'🎄 Part {x}: {sol} :: {t1-t0:.6f} sec')


if __name__ == '__main__':
     main(sys.argv[1:])
