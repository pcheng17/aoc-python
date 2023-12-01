from aocd import get_data
raw_data = get_data(day=1, year=2023)

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(raw_data):
    return raw_data.splitlines()

replace_dict = {
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

def replace_numbers(string):
    for k, v in replace_dict.items():
        string = string.replace(k, v)
    return string

def find_number(string):
    for c in string:
        if c.isdigit():
            first = c
            break    

    for c in string[::-1]:
        if c.isdigit():
            last = c
            break
    
    return int(first + last)

def part_a(input):
    return sum([find_number(line) for line in input])

def part_b(input):
    return sum([find_number(replace_numbers(line)) for line in input])
