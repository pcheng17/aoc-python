import sympy
from itertools import combinations

def parse(input):
    data = input.splitlines()
    hailstones = []
    for row in data:
        p, v = row.split('@')
        hailstones.append((
            tuple(map(int, p.split(','))),
            tuple(map(int, v.split(',')))
        ))
    return hailstones

def part_a(input):
    hailstones = parse(input)

    min_bound = 200000000000000
    max_bound = 400000000000000

    total = 0
    for (p, v), (q, u) in combinations(hailstones, 2):
        p0, p1, _ = p
        q0, q1, _ = q
        v0, v1, _ = v
        u0, u1, _ = u

        d = (u0*v1 - u1*v0)
        if d == 0:
            continue

        t = (p0*u1 - p1*u0 - q0*u1 + q1*u0) / d
        s = (p0*v1 - p1*v0 - q0*v1 + q1*v0) / d

        if t < 0 or s < 0:
            continue

        x = p0 + t*v0
        y = p1 + t*v1

        if min_bound <= x <= max_bound and min_bound <= y <= max_bound:
            total += 1

    return total

def part_b(input):
    hailstones = parse(input)

    q = sympy.symbols('q0 q1 q2')
    u = sympy.symbols('u0 u1 u2')
    t = sympy.symbols('t0 t1 t2')

    equations = [
        sympy.Eq(hailstones[i][0][j] + t[i] * hailstones[i][1][j], q[j] + u[j] * t[i])
        for i in range(3) for j in range(3)
    ]

    solution = sympy.solve(equations, (*q, *u, *t))
    return sum(solution[0][:3])
