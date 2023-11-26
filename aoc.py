import click
import datetime
import importlib
import os
import sys
import time

from datetime import datetime
from pathlib import Path
from textwrap import dedent

from aocd.utils import AOC_TZ
from aocd import exceptions


def print_banner(year, day):
    days_til = 25 - int(day)
    date_str = datetime(year, 12, int(day)).strftime('%B %d, %Y')
    countdown_str = f'{days_til} day{"" if days_til == 1 else "s"} til Christmas' if days_til > 0 else 'Merry Christmas!'
    title_str = f'|        Advent of Code :: {date_str} :: {countdown_str}       |'
    separator = '+' + '-' * (len(title_str) - 2) + '+'
    print(separator)
    print(title_str)
    print(separator)

def get_current_year():
    return datetime.now(tz=AOC_TZ).year

def get_current_day():
    return datetime.now(tz=AOC_TZ).day

def get_default_day():
    return min(get_current_day(), 25) if datetime.now(tz=AOC_TZ).month == 12 else 1

def run(year, day, parts):
    """Run the solution for the specified Advent of Code problem"""

    if not os.path.exists(f'./{year}/q{day:02d}.py'):
        sys.exit(f'Solution code doesn\'t exist.')

    try:
        module = importlib.import_module(f'{year}.q{day:02d}')
    except exceptions.PuzzleLockedError as e:
        print(e)
        sys.exit()

    input_data = module.parse(module.data)
    parts_to_run = [p.upper() for p in parts] if parts else ['A', 'B']

    print_banner(year, day)

    for part in sorted(parts_to_run):
        solve_part = f'solve{part}'
        if hasattr(module, solve_part):
            t0 = time.time()
            answer = getattr(module, solve_part)(input_data)
            t1 = time.time()
            elapsed_time_ms = (t1 - t0) * 1000
            print(f'🎄 Part {part}: {answer} :: {elapsed_time_ms:.2f} ms')
        else:
            print(f'No solution function found for Part {part}.')

def create(year, day):
    """Create the solution scaffold for a particular Advent of Code problem."""

    filepath = Path(__file__).parent / f'{year}' / f'q{day:02d}.py'

    if filepath.exists():
        return False

    if not filepath.parents[0].exists():
        filepath.parents[0].mkdir(parents=True, exist_ok=True)

    filepath.write_text(
        dedent('''\
            from aocd import get_data
            data = get_data(day={day}, year={year})

            # This always returns a list of strings, where the strings were separated by newlines 
            # in the input data.
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
                print(f'Part A: {{solveA(input)}}')
                print(f'Part B: {{solveB(input)}}')
            ''').format(day=day, year=year)
        )
    
    click.echo(f'Created {filepath}')
    return True

@click.command()
@click.argument('year', type=click.IntRange(2015, get_current_year()))
@click.argument('day', type=click.IntRange(1, 25))
@click.argument('parts', nargs=-1)
def cli(year, day, parts):
    """Advent of Code CLI."""
    if not create(year, day):
        run(year, day, parts)

if __name__ == '__main__':
    cli()
