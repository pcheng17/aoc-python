import functools

@functools.lru_cache(maxsize=None)
def dfs(word, subwords, start_pos = 0):
    if start_pos == len(word):
        return True

    for subword in subwords:
        if word[start_pos:].startswith(subword):
            if dfs(word, subwords, start_pos + len(subword)):
                return True

    return False

def dfs_find_all(word, subwords, start_pos, path = []):
    if start_pos == len(word):
        return path.copy()

    all_paths = []

    for subword in subwords:
        if word[start_pos:].startswith(subword):
            path.append(subword)
            tmp = dfs_find_all(word, subwords, start_pos + len(subword), path)
            all_paths.extend(tmp)
            path.pop()

    return all_paths

def part_a(input):
    # with open('./2024/bonsoon19.txt') as f:
    #     input = f.read()
    a, b = input.split("\n\n")
    subwords = tuple(a.split(', '))
    words = b.split('\n')
    total = 0
    for w in words:
        if dfs(w, subwords):
            total += 1
    return total

def part_b(input):
    a, b = input.split("\n\n")
    subwords = a.split(', ')
    words = b.split('\n')
    total = 0
    # for w in words:
    #     if dfs(w, subwords):
    #         tmp = dfs_find_all(w, subwords, 0)
    #         tmp = ''.join(tmp)
    #         total += tmp.count(w)
    return total
