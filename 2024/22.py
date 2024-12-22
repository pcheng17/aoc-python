import itertools

def generate(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n

def get_prices(n):
    out = [n % 10]
    for _ in range(2000):
        out.append((n := generate(n)) % 10)
    return out

def asdf(prices):
    memo = dict()
    deltas = [b - a for a, b in itertools.pairwise(prices)]
    for i in range(len(deltas) - 3):
        seq = tuple(deltas[i:i+4])
        price = prices[i+4]
        if seq not in memo:
            memo[seq] = price
    return memo

def part_a(input):
    data = input.splitlines()
    total = 0
    for row in data:
        n = int(row)
        for _ in range(2000):
            n = generate(n)
        total += n
    return total


def part_b(input):
    data = input.splitlines()
    memos = [asdf(get_prices(int(row))) for row in data]

    all_keys = set()
    for memo in memos:
        all_keys.update(memo.keys())

    qwer = []
    for k in all_keys:
        qwer.append(sum(memo[k] for memo in memos if k in memo))

    return max(qwer)

