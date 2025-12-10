from itertools import combinations
import numpy as np

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

def solve_joltages_greedy(goal, basis_vectors):
    current_goal = goal.copy()
    presses = 0
    while any(g > 0 for g in current_goal):
        best_vector = None
        best_reduction = -1
        for v in basis_vectors:
            fits = all(g >= b for g, b in zip(current_goal, v))
            if not fits:
                continue
            reduction = sum(min(g, b) for g, b in zip(current_goal, v))
            if reduction > best_reduction:
                best_reduction = reduction
                best_vector = v
        if best_vector is None or best_reduction == 0:
            return float('inf')
        print(f"Using basis vector {best_vector} to reduce goal {current_goal}")
        max_use = min(g for g, b in zip(current_goal, best_vector) if b > 0)
        current_goal -= max_use * best_vector
        presses += max_use
    return presses

def solve_joltages(goal, basis_vectors):
    memo = {}
    def recurse(current_goal):
        key = current_goal.tobytes()
        if key in memo:
            return memo[key]

        if all(g == 0 for g in current_goal):
            memo[key] = 0
            return 0

        best = float('inf')
        for v in basis_vectors:
            new_goal = current_goal - v
            if all (g >= 0 for g in new_goal):
                presses = recurse(new_goal)
                best = min(best, presses + 1)

        memo[key] = best
        return best
    return recurse(goal)

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

    count = 0
    for i in range(len(all_lights)):
        print(f"Processing case {i+1}/{len(all_lights)}")
        goal_lights = all_lights[i]
        goal_joltages = all_joltages[i]
        buttons = all_buttons[i]
        basis_vectors = [get_basis_vector(len(goal_lights), b) for b in buttons]
        count += solve_joltages_greedy(goal_joltages, basis_vectors)

    return count
