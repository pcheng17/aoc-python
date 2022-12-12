def nlargest(n, iterable, key=None):
    return sorted(iterable, key=key, reverse=True)[:n]

def nsmallest(n, iterable, key=None):
    return sorted(iterable, key=key, reverse=False)[:n]
