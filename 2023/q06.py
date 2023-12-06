from aocd import get_data


def get_input():
    return get_data(day=6, year=2023)

def part_a(input):
    time_str, dist_str = input.splitlines()
    times = list(map(int, [x for x in time_str.split(':')[1].split(' ') if x != '']))
    distances = list(map(int, [x for x in dist_str.split(':')[1].split(' ') if x != '']))

    result = 1
    for t, d in zip(times, distances):
        total = 0
        for h in range(0, t+1):
            will_travel = (t - h) * h
            if will_travel > d:
                total += 1
        result *= total
    return result
                

def part_b(input):
    time_str, dist_str = input.splitlines()
    times = [x for x in time_str.split(':')[1].split(' ') if x != '']
    distances = [x for x in dist_str.split(':')[1].split(' ') if x != '']
    time = int(''.join(times))
    distance = int(''.join(distances))

    total = 0    
    for h in range(0, time+1):
        will_travel = (time - h) * h
        if will_travel > distance:
            total += 1
    return total
