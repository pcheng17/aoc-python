import argparse
import sys

from datetime import datetime
from pathlib import Path
from textwrap import dedent

from aocd.utils import AOC_TZ


def main():
    now = datetime.now(tz=AOC_TZ)
    validYears = range(2015, now.year + int(now.month >= 11))
    validDays = range(1, 26)

    parser = argparse.ArgumentParser(
            description='Helper method for creating solution files from a template for a specified day')
    parser.add_argument(
            'year',
            nargs='?',
            type=int,
            default=validYears[-1],
            help='2015-%(default)s (default: %(default)s)')
    parser.add_argument(
            'day', 
            nargs='?', 
            type=int, 
            default=min(now.day, 25) if now.month==12 else 1, 
            help='1-25 (default: %(default)s)')
    parser.add_argument(
            '-f',
            '--force',
            action='store_true',
            help='create the file template even if it already exists')
    args = parser.parse_args()

    # Be forgiving of the order of inputs
    if args.day in validYears and args.year in validDays:
        args.day, args.year = args.year, args.day
    if args.day not in validDays or args.year not in validYears:
        parser.print_usage()
        parser.exit(1)

    year, day = args.year, args.day
    fileToCreate = Path(__file__).parent / f'{year}' / f'q{day:02d}.py'

    if not fileToCreate.parents[0].exists():
        fileToCreate.parents[0].mkdir(parents=True, exist_ok=True)

    if fileToCreate.exists():
        if not args.force:
            sys.exit(f'{fileToCreate} already exists! (use -f to overwrite)')

    fileToCreate.write_text(
        dedent('''\
            from aocd import data


            def parse(data):
                return data.splitlines()


            def partA(input):
                pass


            def partB(input):
                pass


            def solveA(input):
                return partA(input)


            def solveB(input):
                return partB(input)


            if __name__ == '__main__':
                input = parse(data)
                print(f'Part A: {solveA(input)}')
                print(f'Part B: {solveB(input)}')
            ''')
        )
    return


if __name__ == '__main__':
    main()
