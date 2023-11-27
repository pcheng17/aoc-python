from aocd import get_data
raw_data = get_data(day=2, year=2020)

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(input):
    data_list = input.splitlines()
    data = [] 
    for row in data_list:
        x, y, z = row.split()
        a, b = map(int, x.split('-'))
        letter = y[:-1]
        data.append((a, b, letter, z))
    return data

def part_a(input):
    valid = 0
    for a, b, letter, password in input:
        count = password.count(letter)
        if a <= count and count <= b:
            valid += 1
    return valid

def part_b(input):
    valid = 0
    for a, b, letter, password in input:
        if password[a-1] == letter and password[b-1] != letter:
            valid += 1
        elif password[a-1] != letter and password[b-1] == letter:
            valid += 1
    return valid
