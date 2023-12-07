from collections import defaultdict
import functools

card_rank_part_a = {
    'A': 12,
    'K': 11, 
    'Q': 10, 
    'J': 9, 
    'T': 8, 
    '9': 7, 
    '8': 6, 
    '7': 5, 
    '6': 4, 
    '5': 3, 
    '4': 2, 
    '3': 1, 
    '2': 0 
}

card_rank_part_b = {
    'A': 12,
    'K': 11, 
    'Q': 10, 
    'T': 9, 
    '9': 8, 
    '8': 7, 
    '7': 6, 
    '6': 5, 
    '5': 4, 
    '4': 3, 
    '3': 2, 
    '2': 1, 
    'J': 0, 
}

def encode_hand_part_a(h):
    d = defaultdict(lambda: 0)
    for x in h:
        d[x] += 1
    return (max(d.values()), len(d))

def encode_hand_part_b(h):
    njs = h.count('J')
    s = set(c for c in h if c != 'J')

    if njs == 5 or njs == 4:
        return (5, 1)
    elif njs == 3:
        if len(s) == 2:
            return (4, 2)
        if len(s) == 1:
            return (5, 1)            
    elif njs == 2:
        if len(s) == 3:
            return (3, 3)
        if len(s) == 2:
            return (4, 2)
        if len(s) == 1:
            return (5, 1)
    elif njs == 1:
        if len(s) == 4:
            return (2,4)
        if len(s) == 3: 
            return (3,3)
        if len(s) == 2:
            ss = list(s)
            if h.count(ss[0]) == 2:
               return (3, 2) 
            else:
                return (4, 2)
        if len(s) == 1:
            return (5, 1)
    else:
        return encode_hand_part_a(h)

def card_compare_part_a(a, b):
    for x, y in zip(a, b):
        if card_rank_part_a[x] < card_rank_part_a[y]:
            return -1
        elif card_rank_part_a[x] == card_rank_part_a[y]:
            continue 
        else:
            return 1
    return 0

def card_compare_part_b(a, b):
    for x, y in zip(a, b):
        if card_rank_part_b[x] < card_rank_part_b[y]:
            return -1
        elif card_rank_part_b[x] == card_rank_part_b[y]:
            continue 
        else:
            return 1
    return 0

def hand_compare_part_a(a, b):
    da = encode_hand_part_a(a[0])
    db = encode_hand_part_a(b[0])
    if da[0] < db[0]:
        return -1
    elif da[0] == db[0]:
        if da[1] < db[1]:
            return 1
        elif da[1] == db[1]:
            return card_compare_part_a(a[0], b[0])
        else:
            return -1
    else:
        return 1

def hand_compare_part_b(a, b):
    da = encode_hand_part_b(a[0])
    db = encode_hand_part_b(b[0])
    if da[0] < db[0]:
        return -1
    elif da[0] == db[0]:
        if da[1] < db[1]:
            return 1
        elif da[1] == db[1]:
            return card_compare_part_b(a[0], b[0])
        else:
            return -1
    else:
        return 1

def part_a(input):
    data = [(x, int(y)) for x, y in (line.split() for line in input.splitlines())]
    data = sorted(data, key=functools.cmp_to_key(hand_compare_part_a))
    return sum(r * b for r, (h, b) in enumerate(data, 1))

def part_b(input):
    data = [(x, int(y)) for x, y in (line.split() for line in input.splitlines())]
    data = sorted(data, key=functools.cmp_to_key(hand_compare_part_b))
    return sum(r * b for r, (h, b) in enumerate(data, 1))
