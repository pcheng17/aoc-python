from itertools import combinations
import numpy as np
from scipy.optimize import linprog

def apply_button(lights, button):
    for b in button:
        lights[b] = 1 - lights[b]
    return lights

def get_basis_vector(num_lights, buttons):
    basis = [0] * num_lights
    basis = np.array(basis, dtype=np.int64)
    for b in buttons:
        basis[b] = 1
    return basis

def part_a(input):
    all_lights = []
    all_buttons = []
    all_joltages = []
    for row in input.splitlines():
        elements = row.split(' ')
        all_lights.append( [0 if c == '.' else 1 for c in elements[0][1:-1]] )
        z = []
        for e in elements[1:-1]:
            z.append(list(map(int, e[1:-1].split(','))))
        all_buttons.append(z)
        all_joltages.append(list(map(int, elements[-1][1:-1].split(','))))

    count = 0
    for i in range(len(all_lights)):
        goal = all_lights[i]
        buttons = all_buttons[i]
        n_buttons = len(buttons)
        found = False
        for sz in range(0, n_buttons + 1):
            for subset in combinations(range(n_buttons), sz):
                result = [0] * len(goal)
                for s in subset:
                    result = apply_button(result, buttons[s])
                if result == goal:
                    count += sz
                    found = True
                    break
            if found:
                break
    return count

def get_system(num_lights, buttons):
    A = []
    for b in buttons:
        A.append(get_basis_vector(num_lights, b))
    A = np.transpose(np.array(A, dtype=np.int64))
    return A

def part_b(input):
    all_lights = []
    all_buttons = []
    all_joltages = []
    for row in input.splitlines():
        elements = row.split(' ')
        all_lights.append(np.array([0 if c == '.' else 1 for c in elements[0][1:-1]], dtype=np.int64))
        z = []
        for e in elements[1:-1]:
            z.append(list(map(int, e[1:-1].split(','))))
        all_buttons.append(z)
        all_joltages.append(np.array(list(map(int, elements[-1][1:-1].split(','))), dtype=np.int64))

    ans = 0
    for i, (lights, buttons, joltages) in enumerate(zip(all_lights, all_buttons, all_joltages)):
        b = np.reshape(joltages, (len(joltages), 1))
        c = np.ones(len(buttons), dtype=np.int64)
        A = get_system(len(lights), buttons)
        result = linprog(c, A_eq=A, b_eq=b, integrality=c)
        ans += sum(result.x)

    return ans
