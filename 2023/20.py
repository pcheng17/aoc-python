from collections import deque, defaultdict
from math import lcm


def parse(input):
    nodes = {}
    ntypes = {}
    # conjunctions = []
    # flip_flops = []
    for line in input.splitlines():
        lhs, rhs = line.split(' -> ')
        if 'broadcast' in lhs:
            nodes[lhs] =  rhs.split(', ')
        else:
            nodes[lhs[1:]] = rhs.split(', ')

        if '&' in lhs:
            # conjunctions.append(lhs[1:])
            ntypes[lhs[1:]] = 'c'

        if '%' in lhs:
            # flip_flops.append(lhs[1:])
            ntypes[lhs[1:]] = 'f'


    conjunction_inputs = defaultdict(list)
    for c in [x for x, y in ntypes.items() if y == 'c']:
        for k, v in nodes.items():
            if c in v:
                conjunction_inputs[c].append(k)

    # Intialize states for all flip_flops
    states = {k: 0 for k in [x for x, y in ntypes.items() if y == 'f']}

    # Initialize memory for conjunctions
    memory = {k: 0 for k in nodes}

    return nodes, ntypes, conjunction_inputs, states, memory


def part_a(input):
    nodes, ntypes, conjunction_inputs, states, memory = parse(input)

    # Solve
    pulse_count = [0, 0]
    queue = deque()

    for i in range(1000):
        queue.extend(('broadcaster', 0, n) for n in nodes['broadcaster'])
        pulse_count[0] += 1

        while queue:
            s, p, d = queue.popleft()
            pulse_count[p] += 1
            if d in ntypes:
                if ntypes[d] == 'f':
                    if p == 0:
                        states[d] = 1 - states[d]
                        queue.extend((d, states[d], nbrs) for nbrs in nodes[d])
                else:
                    memory[s] = p
                    pulse = int(all([memory[x] for x in conjunction_inputs[d]]))
                    queue.extend((d, 1 - pulse, nbrs) for nbrs in nodes[d])

    return pulse_count[0] * pulse_count[1]


def part_b(input):
    nodes, ntypes, conjunction_inputs, states, memory = parse(input)

    # Solve
    periods = []

    for zz in conjunction_inputs['vr']:
        queue = deque()
        idx = 0

        for k in states:
            states[k] = 0
        for k in memory:
            memory[k] = 0

        while True:
            idx += 1
            found = False
            queue.extend(('broadcaster', 0, n) for n in nodes['broadcaster'])

            while queue:
                s, p, d = queue.popleft()
                if s == zz and p == 1:
                    periods.append(idx)
                    found = True
                    break

                if d in ntypes:
                    if ntypes[d] == 'f':
                        if p == 0:
                            states[d] = 1 - states[d]
                            queue.extend((d, states[d], nbrs) for nbrs in nodes[d])
                    else:
                        memory[s] = p
                        pulse = int(all([memory[x] for x in conjunction_inputs[d]]))
                        queue.extend((d, 1 - pulse, nbrs) for nbrs in nodes[d])

            if found:
                break

    return lcm(*periods)
