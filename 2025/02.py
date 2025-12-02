def check_invalid_a(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False
    else:
        mid = len(num_str) // 2
        left, right = num_str[:mid], num_str[mid:]
        return left == right

def check_invalid_b(num):
    num_str = str(num)
    for k in range(1, len(num_str)):
        if len(num_str) % k != 0:
            continue
        else:
            parts = [num_str[i:i+k] for i in range(0, len(num_str), k)]
            if all(part == parts[0] for part in parts):
                return True

def part_a(input):
    data = input.split(',')
    ranges = [list(map(int, r.split('-'))) for r in data]
    ans = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if check_invalid_a(i):
                ans += i
    return ans

def part_b(input):
    data = input.split(',')
    ranges = [list(map(int, r.split('-'))) for r in data]
    ans = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if check_invalid_b(i):
                ans += i
    return ans
