def part_a(input):
    a, b = input.split("\n\n")
    subwords, words = tuple(a.split(', ')), b.split('\n')

    seen = set()
    def dfs(w):
        if len(w) == 0 or w in seen:
            return True
        for sw in subwords:
            if w.startswith(sw) and dfs(w[len(sw):]):
                seen.add(w)
                return True
        return False

    return sum([dfs(w) for w in words])

def part_b(input):
    a, b = input.split("\n\n")
    subwords, words = a.split(', '), b.split('\n')

    seen = {}
    def find_all(w):
        if len(w) == 0:
            return 1
        if w in seen:
            return seen[w]
        count = 0
        for sw in subwords:
            if w.startswith(sw):
                count += find_all(w[len(sw):])
        seen[w] = count
        return count

    return sum([find_all(w) for w in words])
