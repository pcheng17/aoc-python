from aocd import data

cals = []
for chunk in data.split("\n\n"):
    cals.append(sum(map(int, chunk.split())))

cals = sorted(cals)

print(f"Part A: {cals[-1]}")
print(f"Part B: {cals[-3] + cals[-2] + cals[-1]}")

