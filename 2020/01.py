def parse(input):
    return sorted(list(map(int, input.splitlines())))

def part_a(input):
    data = parse(input)
    i = 0
    j = len(data) - 1
    while i < j:
        if data[i] + data[j] == 2020:
            return data[i] * data[j]
        elif data[i] + data[j] < 2020:
            i += 1
        else:
            j -= 1

def part_b(input):
    data = parse(input)
    for i in range(len(data)):
        j = i + 1
        k = len(data) - 1
        while j < k:
            if data[i] + data[j] + data[k] == 2020:
                return data[i] * data[j] * data[k]
            elif data[i] + data[j] + data[k] < 2020:
                j += 1
            else:
                k -= 1
