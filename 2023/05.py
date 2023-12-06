def check_for_overlap(m):
    for i in range(0, len(m)-1):
        if m[i][1] + m[i][2] - 1 >= m[i+1][1]:
            print(m[i], m[i+1])

def part_a(input):
    a, b, c, d, e, f, g, h = input.split('\n\n')
    seeds = [int(x) for x in a.split(':')[1].split(' ') if len(x) != 0]

    map_data = [
        [tuple(map(int, x.split(' '))) for x in b.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in c.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in d.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in e.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in f.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in g.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in h.splitlines()[1:]],
    ]

    for m in map_data:
        new_seeds = []
        for s in seeds:
            found = False
            for dst, src, rng in m:
                if src <= s < src + rng:
                    new_seeds.append(dst + (s - src))
                    found = True
                    break
            if not found:
                new_seeds.append(s)
        seeds = new_seeds

    return min(seeds)

def part_b(input):
    a, b, c, d, e, f, g, h = input.split('\n\n')
    seeds = [int(x) for x in a.split(':')[1].split(' ') if len(x) != 0]
    seed_rngs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    
    map_data = [
        [tuple(map(int, x.split(' '))) for x in b.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in c.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in d.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in e.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in f.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in g.splitlines()[1:]],
        [tuple(map(int, x.split(' '))) for x in h.splitlines()[1:]],
    ]
    
    current = 0
    t = 0
    while True:
        for m in reversed(map_data):
            for dst, src, rng in m:
                if dst <= t < dst + rng:
                    t = src + (t - dst)
                    break
            # If t was never found in the map, then 
            # seed -> seed rule leaves t unchanged.
        
        for s, r in seed_rngs:
            if s <= t < s + r:
                return current
        
        current += 1
        t = current

# This version is not totally right in that it doesn't implement the mapping functions
# according to what is defined in the problem statement. However, it does produce the right
# answer...

# def part_b(input):
#     a, b, c, d, e, f, g, h = input.split('\n\n')
#     seeds = [int(x) for x in a.split(':')[1].split(' ') if len(x) != 0]
#     seed_rngs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    
#     map_data = [
#         [tuple(map(int, x.split(' '))) for x in b.splitlines()[1:]],
#         [tuple(map(int, x.split(' '))) for x in c.splitlines()[1:]],
#         [tuple(map(int, x.split(' '))) for x in d.splitlines()[1:]],
#         [tuple(map(int, x.split(' '))) for x in e.splitlines()[1:]],
#         [tuple(map(int, x.split(' '))) for x in f.splitlines()[1:]],
#         [tuple(map(int, x.split(' '))) for x in g.splitlines()[1:]],
#         [tuple(map(int, x.split(' '))) for x in h.splitlines()[1:]],
#     ]

#     for m in map_data:
#         new_seed_rngs = []    
#         for seed_start, seed_rng in seed_rngs:
#             for dst, src, rng in m:
#                 if src <= seed_start < src + rng:
#                     new_seed_rngs.append((dst + (seed_start - src), min(seed_rng, (src + rng) - seed_start)))
#                 elif seed_start < src < seed_start + seed_rng:
#                     new_seed_rngs.append((dst, min(rng, seed_rng - (src - seed_start))))
#         seed_rngs = new_seed_rngs
    
#     return(min([x[0] for x in seed_rngs]))
