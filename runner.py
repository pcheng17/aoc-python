import importlib
import time
import sys



args = sys.argv[1:]

part = None
if len(args) == 2:
    year, day = args
else:
    year, day, *part = args

print("==== Merry Christmas! ====\n")
print(f'Day {day}')

module = importlib.import_module(f'{year}.q{day}')
input = module.parse(module.data)

if part is not None:
    if part[0] == 'A':
        t0 = time.time()
        solA = module.solveA(input)
        t1 = time.time()
        print(f'  Part A: {solA} ::: {t1 - t0 : .6f} sec')
    elif part[0] == 'B':
        t0 = time.time()
        solB = module.solveB(input)
        t1 = time.time()
        print(f'  Part B: {solB} ::: {t1 - t0 : .6f} sec')
else:
    t0 = time.time()
    solA = module.solveA(input)
    tA = time.time() - t0
    print(f'  Part A: {solA} ::: {tA : .6f} sec')
    t0 = time.time()
    solB = module.solveB(input)
    tB = time.time() - t0
    print(f'  Part B: {solB} ::: {tB : .6f} sec')
