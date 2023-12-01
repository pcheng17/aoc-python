import hashlib
from aocd import get_data
raw_data = get_data(day=4, year=2015)


# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(data):
    return data.splitlines()

def find_solution(secret_key, prefix):
    num = 0
    while True:
        candidate = f'{secret_key}{num}'
        tmp = hashlib.md5(candidate.encode('utf-8')).hexdigest()
        if tmp.startswith(prefix):
            return num
        num += 1

def part_a(input):
    return find_solution(input[0], '00000')

def part_b(input):
    return find_solution(input[0], '000000')
