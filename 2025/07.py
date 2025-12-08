from collections import defaultdict

def part_a(input):
    data = input.splitlines()
    total_rows = len(data)
    startCol = data[0].index('S')
    tachyon_cols = set([startCol])
    row = 1
    ans = 0
    while row < total_rows - 1:
        new_tachyon_cols = set()
        for col in tachyon_cols:
            if data[row + 1][col] == '^':
                ans += 1
                new_tachyon_cols.add(col + 1)
                new_tachyon_cols.add(col - 1)
            else:
                new_tachyon_cols.add(col)
        tachyon_cols = new_tachyon_cols
        row += 1
    return ans

def part_b(input):
    data = input.splitlines()
    total_rows = len(data)
    startCol = data[0].index('S')
    tachyon_cols = {startCol : 1}
    row = 1
    while row < total_rows - 1:
        new_tachyon_cols = defaultdict(int)
        for col in tachyon_cols:
            if data[row + 1][col] == '^':
                new_tachyon_cols[col + 1] += tachyon_cols[col]
                new_tachyon_cols[col - 1] += tachyon_cols[col]
            else:
                new_tachyon_cols[col] += tachyon_cols[col]
        tachyon_cols = new_tachyon_cols
        row += 1
    return sum(tachyon_cols.values())
