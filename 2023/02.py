from aocd import get_data


def get_input():
    return get_data(day=2, year=2023)

def part_a(input):
    elf_data = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    total = 0
    for line in input.splitlines():
        possible = True
        a, b = line.split(':')
        game_id = a.split()[1]
        for game in b.split(';'):
            for draw in game.split(','):
                num, color = draw.split()
                if elf_data[color] < int(num):
                    possible = False

        if possible:
            total += int(game_id)

    return total

def part_b(input):
    total = 0
    for line in input.splitlines():
        color_dict = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        a, b = line.split(':')
        for game in b.split(';'):
            for draw in game.split(','):
                num, color = draw.split()
                if int(num) > color_dict[color]:
                    color_dict[color] = int(num)
        
        power = 1
        for v in color_dict.values():
            power *= v
        total += power 

    return total
