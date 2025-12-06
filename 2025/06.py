ops = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
}

def part_a(input):
    data = []
    for row in input.splitlines():
        data.append(row.split())
    asdf = list(zip(*data))
    ans = 0
    for row in asdf:
        z = 0
        z += int(row[0])
        op = row[-1]
        for i in range(1, len(row) - 1):
            z = ops[op](z, int(row[i]))
        ans += z
    return ans

def part_b(input):
    data = []
    for row in input.splitlines():
        data.append([c for c in row])

    operations = [c for c in data[-1] if c != ' ']

    ans = 0
    cols = len(data[0])
    rows = len(data) - 1
    nums = []
    opsidx = len(operations) - 1
    for j in range(cols-1, -1, -1):
        numstr = ''
        for i in range(rows):
            if data[i][j] is not ' ':
                numstr += data[i][j]
        numstr = numstr.strip()
        if numstr:
            nums.append(numstr)
        else:
            # We're done, do the operation
            z = int(nums[0])
            for k in range(1, len(nums)):
                z = ops[operations[opsidx]](z, int(nums[k]))
            opsidx -= 1
            ans += z
            nums = []
    if nums:
        z = int(nums[0])
        for k in range(1, len(nums)):
            z = ops[operations[opsidx]](z, int(nums[k]))
        ans += z
    return ans

