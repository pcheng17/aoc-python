run YEAR DAY *FLAGS:
    watchexec -c -r -w ./{{YEAR}} "./aoc.py --year={{YEAR}} --day={{DAY}} {{FLAGS}}"
