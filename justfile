run YEAR DAY:
    watchexec -c -w ./{{YEAR}} "python aoc.py --year={{YEAR}} --day={{DAY}}"

test YEAR DAY:
    watchexec -c -w ./{{YEAR}} "python aoc.py --year={{YEAR}} --day={{DAY}} -e"

