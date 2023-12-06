def parse(data):
    return list(map(int, data.splitlines()))

def part_a(input):
    data = parse(input)
    return sum([b > a for a, b in zip(data, data[1:])])

def part_b(input):
    data = parse(input)
    windowSum = sum([data[i] for i in range(3)])
    count = 0
    for i in range(3, len(data)):
        tmp = windowSum - data[i-3] + data[i]
        if tmp > windowSum:
            count += 1
        windowSum = tmp
    return count
