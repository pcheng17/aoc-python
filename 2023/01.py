def replace_numbers(string):
    m = {
        'one':   'o1e',
        'two':   't2o',
        'three': 't3e',
        'four':  'f4r',
        'five':  'f5e',
        'six':   's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine':  'n9e'   
    }
    for k, v in m.items():
        string = string.replace(k, v)
    return string

def find_number(string):
    d = [c for c in string if c.isdigit()]
    return int(d[0] + d[-1])

def part_a(input):
    return sum([find_number(line) for line in input.splitlines()])

def part_b(input):
    return sum([find_number(replace_numbers(line)) for line in input.splitlines()])
