from aocd import get_data
raw_data = get_data(day=5, year=2020)

# This always returns a list of strings, where the strings were separated by newlines 
# in the input data.
def parse(raw_data):
    return raw_data.splitlines()

def decode(string):
    row_binary_str = ''.join(['1' if c == 'B' else '0' for c in string[0:7]])
    col_binary_str = ''.join(['1' if c == 'R' else '0' for c in string[7:]])
    return int(row_binary_str, 2), int(col_binary_str, 2)

def compute_id(row, col):
    return row * 8 + col

def part_a(input):
    all_decoded = [decode(x) for x in input]
    ids = [compute_id(r, c) for r, c in all_decoded]
    return max(ids)

def part_b(input):
    all_decoded = [decode(x) for x in input]
    ids = [compute_id(r, c) for r, c in all_decoded]
    ids = sorted(ids)
    all_seats = list(range(ids[0], ids[-1] + 1))
    missing_seats = [x for x in all_seats if x not in ids]
    return missing_seats[0]
