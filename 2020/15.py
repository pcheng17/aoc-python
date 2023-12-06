from collections import defaultdict


def parse(input):
    return list(map(int, input.split(',')))

def play_game(start_numbers, turns):
    history = defaultdict(list)
    for i, n in enumerate(start_numbers,  1):
        history[n].append(i)
    
    last_number = start_numbers[-1]
    for turn in range(len(start_numbers) + 1, turns + 1):
        if len(history[last_number]) == 1:
            history[0].append(turn)
            last_number = 0
        else:
            new_number = history[last_number][-1] - history[last_number][-2]
            history[new_number].append(turn)
            last_number = new_number
    
    return last_number

def part_a(input):
    return play_game(parse(input), 2020)

def part_b(input):
    return play_game(parse(input), 30000000)
