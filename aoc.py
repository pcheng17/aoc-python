import click
import datetime
import importlib
import os
import sys
import time

from datetime import datetime
from pathlib import Path
from prettytable import PrettyTable
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

def print_timing_table(timing):
    table = PrettyTable()
    table.field_names = ['Problem', 'Part a (ms)', 'Part b (ms)', 'Total (ms)']
    table.align['Problem'] = 'l'
    total_a = 0
    total_b = 0
    for i, (a, b) in enumerate(timing, 1):
        table.add_row([f'Day {i}', f'{a:.2f}', f'{b:.2f}', f'{a+b:.2f}'], divider=True if i == 25 else False)
        total_a += a
        total_b += b
    total = total_a + total_b
    table.add_row(['Total (ms)', f'{total_a:.2f}', f'{total_b:.2f}', f'{total_a+total_b:.2f}'])
    print(table)

def run(year, day, parts):
    """Run the solution for the specified Advent of Code problem"""

    if not os.path.exists(f'./{year}/q{day:02d}.py'):
        sys.exit(f'Solution code doesn\'t exist.')

    module = importlib.import_module(f'{year}.q{day:02d}')

    try:
        raw_input = module.get_input()
    except exceptions.PuzzleLockedError as e:
        print(e)
        sys.exit()

    parts_to_run = set([p.lower() for element in parts for p in element]) if parts else ['a', 'b']

    print_banner(year, day)

    for part in sorted(parts_to_run):
        fn = f'part_{part}'
        if hasattr(module, fn):
            t0 = time.time()
            answer = getattr(module, fn)(raw_input)
            t1 = time.time()
            elapsed_time_ms = (t1 - t0) * 1000
            print(f'🎄 Part {part}: {answer} :: {elapsed_time_ms:.2f} ms')
        else:
            print(f'No solution function found: part_{part}.')

def benchmark(year):
    if not os.path.exists(f'./{year}'):
        sys.exit(f"Solution code for year {year} doesn't exist.")

    timing = []
    for day in range(1, 26):
        if not os.path.exists(f'./{year}/q{day:02d}.py'):
            timing.append((0, 0))
            continue

        module = importlib.import_module(f'{year}.q{day:02d}')

        try:
            raw_input = module.get_input()
        except exceptions.PuzzleLockedError as e:
            timing.append((0, 0))
            continue

        tmp = []
        for part in ['a', 'b']:
            fn = f'part_{part}'
            if hasattr(module, fn):
                t0 = time.time()
                answer = getattr(module, fn)(raw_input)
                t1 = time.time()
                elapsed_time_ms = (t1 - t0) * 1000
                tmp.append(elapsed_time_ms)
            else:
                data.append(0)
        
        timing.append((tmp[0], tmp[1]))

    print_timing_table(timing)
    
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

            
            def get_input():
                return get_data(day={day}, year={year})
 
            def parse(input):
                pass

            def part_a(input):
                data = input.splitlines()

            def part_b(input):
                data = input.splitlines()
            ''').format(day=day, year=year)
        )
    
    click.echo(f'Created {filepath}')
    return True

class PartType(click.ParamType):
    name = 'part'

    def convert(self, value, param, ctx):
        allowed_chars = {'A', 'B', 'a', 'b'}
        if all(char in allowed_chars for char in value):
            return value
        else:
            self.fail(f"{value!r} contains invalid characters. Allowed characters are: A, B, a, b.", param, ctx)

@click.command()
@click.option('--year', '-y', type=click.IntRange(2015, get_current_year()), default=get_current_year())
@click.option('--day', '-d', type=click.IntRange(1, 25), default=get_default_day())
@click.option('--parts', '-p', type=PartType(), default='AB', help="A string that consists only of the characters 'A', 'B', 'a', and 'b'. Defaults to 'AB'.")
@click.option('--bench', '-b', type=click.IntRange(2015, get_current_year()))
def cli(year, day, parts, bench):
    """Advent of Code CLI."""
    if not bench:
        if not create(year, day):
            run(year, day, parts)
    else:
        benchmark(bench)

if __name__ == '__main__':
    cli()
