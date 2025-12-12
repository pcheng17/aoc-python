def triangular_number(n):
    return n * (n + 1) // 2

def part_a(input):
    data = list(map(int, input.split(',')))
    ans = float('inf')
    for k in range(min(data), max(data) + 1):
        fuel = sum(abs(x - k) for x in data)
        ans = min(ans, fuel)
    return ans

def part_b(input):
    data = list(map(int, input.split(',')))
    ans = float('inf')
    for k in range(min(data), max(data) + 1):
        fuel = sum(triangular_number(abs(x - k)) for x in data)
        ans = min(ans, fuel)
    return ans
