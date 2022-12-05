from aocd import data


def parseContainerRow(row):
    return [row[i:i+3].strip(' []') for i in range(0, len(row), 4)]

def parse(data):
    containers, moves = data.split('\n\n')

    labels = containers.split('\n')[-1].split()

    stacks = [[] for _ in range(len(labels))]
    containers = containers.split('\n')[:-1]
    containers.reverse()
    for row in containers:
        for idx, crate in enumerate(parseContainerRow(row)):
            if len(crate):
                stacks[idx].append(crate)
    
    parsedMoves = [];
    for move in moves.split('\n'):
        parsedMoves.append([int(i) for i in move.split() if i.isdigit()])

    return stacks, parsedMoves

def partA(stacks, parsedMoves):
    for move in parsedMoves:
        src = move[1]-1;
        dst = move[2]-1;
        for _ in range(move[0]):
            stacks[dst].append(stacks[src].pop())
    return ''.join([stack[-1] for stack in stacks])

def partB(stacks, parsedMoves):
    for move in parsedMoves:
        src = move[1]-1;
        dst = move[2]-1;
        stacks[dst].extend(stacks[src][-move[0]:])
        del stacks[src][len(stacks[src]) - move[0]:]
    return ''.join([stack[-1] for stack in stacks])


stacks, parsedMoves = parse(data)
print(f'Part A: {partA(stacks, parsedMoves)}')
stacks, parsedMoves = parse(data)
print(f'Part B: {partB(stacks, parsedMoves)}')
