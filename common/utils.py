from math import prod

def nlargest(n, iterable, key=None):
    return sorted(iterable, key=key, reverse=True)[:n]

def nsmallest(n, iterable, key=None):
    return sorted(iterable, key=key, reverse=False)[:n]

def manhattan_dist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

def merge_intervals(intervals):
    if len(intervals) == 0: return []

    intervals = sorted(intervals, key = lambda x : x[0])
    result = []
    result.append(intervals[0])
    for x in intervals[1:]:
        if x[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][-1], x[1])
        else:
            result.append(x)
    return result

def crt(eqs):
    '''Chinese Remainder Theorem'''

    def inv_mod(a, n):
        result = 1
        for _ in range(n - 2):
            result *= a
            result = result % n
        return result

    N = prod(n for _, n in eqs)
    result = 0 
    for a, n in eqs:
        Ni = N // n
        b = inv_mod(Ni, n)
        result += a * Ni * b
    return result % N
