run YEAR DAY *FLAGS:
    watchexec -c -r -w ./{{YEAR}} "./aoc.py --year={{YEAR}} --day={{DAY}} {{FLAGS}}"

run-both YEAR DAY:
    watchexec -c -r -w ./{{YEAR}} "./aoc.py --year={{YEAR}} --day={{DAY}} -e && ./aoc.py --year={{YEAR}} --day={{DAY}}"
