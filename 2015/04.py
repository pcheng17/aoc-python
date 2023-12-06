import hashlib

def find_solution(secret_key, prefix):
    num = 0
    while True:
        candidate = f'{secret_key}{num}'
        tmp = hashlib.md5(candidate.encode('utf-8')).hexdigest()
        if tmp.startswith(prefix):
            return num
        num += 1

def part_a(input):
    return find_solution(input.splitlines()[0], '00000')

def part_b(input):
    return find_solution(input.splitlines()[0], '000000')
