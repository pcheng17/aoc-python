import re


test = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
'''

DIRS = {
    'N': complex(0, -1),
    'E': complex(1, 0),
    'S': complex(0, 1),
    'W': complex(-1, 0)
}

class Player:
    def __init__(self, pos: complex, dir: complex) -> None:
        self.pos = pos
        self.dir = dir

    def col(self) -> int:
        return int(self.pos.real)

    def row(self) -> int:
        return int(self.pos.imag)

    def position(self) -> complex:
        return self.pos

    def setPosition(self, pos: complex) -> None:
        self.pos = pos

    def nextPosition(self) -> complex:
        return self.pos + self.dir

    def direction(self) -> complex:
        return self.dir

    def turnRight(self) -> None:
        self.dir *= complex(0, 1)

    def turnLeft(self) -> None:
        self.dir *= complex(0, -1)

    def stepForward(self) -> None:
        self.pos += self.dir

    def stepBackward(self) -> None:
        self.pos -= self.dir

def weave(lst1, lst2):
    return [sub[item] for item in range(len(lst2)) for sub in [lst1, lst2]]

def parse(data):
    map, directions = data.split('\n\n')

    map = [row for row in map.split('\n')]
    maxLength = len(map[0])
    full_map = [' ' * (maxLength + 2)]
    for row in map:
        if len(row) == maxLength:
            full_map.append(' ' + row + ' ')
        else:
            full_map.append(' ' + row + ' ' * (maxLength - len(row)) + ' ')
    full_map.append(' ' * (maxLength + 2))

    dirLengths = re.findall('[0-9]+', directions.strip())
    dirTurns = re.findall('[A-Z]', directions.strip())

    directions = weave(dirLengths, dirTurns)
    directions.append(dirLengths[-1])

    return (full_map, directions)

def part_a(input):
    full_map, directions = parse(input)

    startRow = 1
    startColumn = len(full_map[1]) - len(full_map[1].lstrip())
    player = Player(complex(startColumn, startRow), complex(1, 0))

    for x in directions:
        if x.isdigit():
            for _ in range(int(x)):
                currPos = player.position()
                nextPos = player.nextPosition()
                nextCol = int(nextPos.real)
                nextRow = int(nextPos.imag)
                match full_map[nextRow][nextCol]:
                    case '.':
                        player.stepForward()
                    case '#':
                        pass
                    case ' ':
                        while full_map[nextRow][nextCol] == ' ':
                            dir = player.direction()
                            dirCol = int(dir.real)
                            dirRow = int(dir.imag)
                            nextRow = (nextRow + dirRow) % len(full_map)
                            nextCol = (nextCol + dirCol) % len(full_map[nextRow])
                        if full_map[nextRow][nextCol] == '#':
                            player.setPosition(currPos)
                        else:
                            player.setPosition(complex(nextCol, nextRow))
        else:
            if x == 'L':
                player.turnLeft()
            elif x == 'R':
                player.turnRight()
            else:
                print('WTF')
                return

    row = player.row()
    col = player.col()
    dirScore = 0
    if player.direction() == DIRS['E']:
        dirScore = 0
    elif player.direction() == DIRS['S']:
        dirScore = 1
    elif player.direction() == DIRS['W']:
        dirScore = 2
    else:
        dirScore = 3

    return 1000 * row + 4 * col + dirScore

def part_b(input):
    full_map, directions = parse(input)
    return 0
