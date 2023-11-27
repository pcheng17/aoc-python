from aocd import get_data
raw_data = get_data(day=1, year=2020)

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(raw_data):
    return sorted(list(map(int, raw_data.splitlines())))

def part_a(input):
    i = 0
    j = len(input) - 1
    while i < j:
        if input[i] + input[j] == 2020:
            return input[i] * input[j]
        elif input[i] + input[j] < 2020:
            i += 1
        else:
            j -= 1

def part_b(input):
    for i in range(len(input)):
        j = i + 1
        k = len(input) - 1
        while j < k:
            if input[i] + input[j] + input[k] == 2020:
                return input[i] * input[j] * input[k]
            elif input[i] + input[j] + input[k] < 2020:
                j += 1
            else:
                k -= 1
