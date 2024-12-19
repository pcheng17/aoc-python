run YEAR DAY:
    watchexec -c -r -w ./{{YEAR}} "python aoc.py --year={{YEAR}} --day={{DAY}}"

test YEAR DAY:
    watchexec -c -r -w ./{{YEAR}} "python aoc.py --year={{YEAR}} --day={{DAY}} -e"

