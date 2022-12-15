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
