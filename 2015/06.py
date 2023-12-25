def part_a(input):
    data = input.splitlines()
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for row in input.splitlines():
        row = row.split(' ')
        if row[0] == 'toggle':
            x1, y1 = map(int, row[1].split(','))
            x2, y2 = map(int, row[3].split(','))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = 1 - grid[i][j]
        else:
            x1, y1 = map(int, row[2].split(','))
            x2, y2 = map(int, row[4].split(','))
            if row[1] == 'on':
                for i in range(x1, x2+1):
                    for j in range(y1, y2+1):
                        grid[i][j] = 1
            else:
                for i in range(x1, x2+1):
                    for j in range(y1, y2+1):
                        grid[i][j] = 0
    return sum(map(sum, grid))

def part_b(input):
    data = input.splitlines()
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for row in input.splitlines():
        row = row.split(' ')
        if row[0] == 'toggle':
            x1, y1 = map(int, row[1].split(','))
            x2, y2 = map(int, row[3].split(','))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] += 2
        else:
            x1, y1 = map(int, row[2].split(','))
            x2, y2 = map(int, row[4].split(','))
            if row[1] == 'on':
                for i in range(x1, x2+1):
                    for j in range(y1, y2+1):
                        grid[i][j] += 1
            else:
                for i in range(x1, x2+1):
                    for j in range(y1, y2+1):
                        grid[i][j] = max(0, grid[i][j] - 1)
    return sum(map(sum, grid))
