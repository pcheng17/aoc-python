from aocd import data
from collections import defaultdict

test = [
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k'
]

def cumulativeJoin(arr):
    result = []
    tmp = ''
    for x in arr:
        tmp += x
        result.append(tmp)
    return result

def parse(lines):
    path = []
    dirs = defaultdict(int)

    for line in lines:
        line = line.strip();
        if len(line) == 0: continue

        if line.startswith('$'):
            _, cmd, *args = line.split()
            if cmd == 'cd':
                dst = args[0]
                if dst == '/':
                    path = ['/']
                elif dst == '..':
                    path.pop()
                else:
                    path.append(dst + '/')
            elif cmd == 'ls':
                pass
        else:
            if line.startswith('dir'):
                pass
            else:
                size, _ = line.split()
                for x in cumulativeJoin(path):
                    dirs[x] += int(size)
    return dirs

def partA(input):
    total = 0
    for x in input.values():
        if x <= 100_000:
            total += x
    return total
     

def partB(input):
    totalAvailable = 70_000_000
    needAtLeast = 30_000_000
    totalUsed = input['/']
    spaceLeft = totalAvailable - totalUsed
    needToClear = needAtLeast - spaceLeft

    if needToClear <= 0:
        return 0
    else:
        sizes = sorted(input.values())
        for x in sizes:
            if x > needToClear:
                return x


lines = data.splitlines()
dirs = parse(lines)
print(f'Part A: {partA(dirs)}')
print(f'Part B: {partB(dirs)}')
