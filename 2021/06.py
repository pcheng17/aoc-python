from collections import defaultdict

def solve(initial_ages, days):
    fish = defaultdict(int)
    for x in initial_ages:
        fish[x] += 1

    for _ in range(days):
        fish_next = defaultdict(int)
        for age, count in fish.items():
            if age > 0:
                fish_next[age - 1] += count
            else:
                fish_next[6] += count
                fish_next[8] += count

        fish = fish_next

    return sum(v for v in fish.values())

def part_a(input):
    data = input.splitlines()
    initial_ages = list(map(int, data[0].split(",")))
    return solve(initial_ages, 80)

def part_b(input):
    data = input.splitlines()
    initial_ages = list(map(int, data[0].split(",")))
    return solve(initial_ages, 256)
