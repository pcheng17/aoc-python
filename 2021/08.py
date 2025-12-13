from collections import defaultdict

num_to_segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

segments_to_num = defaultdict(list)
for i, x in enumerate(num_to_segments):
    segments_to_num[x].append(i)

def part_a(input):
    data = input.splitlines()
    matches = set([num_to_segments[1], num_to_segments[4], num_to_segments[7], num_to_segments[8]])
    ans = 0
    for row in data:
        front, tail = row.split(' | ')
        for x in tail.split(' '):
            if len(x) in matches:
                ans += 1
    return ans

def part_b(input):
    data = input.splitlines()
    ans = 0
    for row in data:
        front, tail = row.split(' | ')
        pattens = front.split(' ')


    return ans
