run YEAR DAY *FLAGS:
    watchexec -c -r -w ./{{YEAR}} "python aoc.py --year={{YEAR}} --day={{DAY}} {{FLAGS}}"
