def sum_board(b):
    total = 0
    for row in b:
        total += sum(x for x in row if x != -1)
    return total

def part_a(input):
    data = input.splitlines('\n\n')
    numbers = [int(x) for x in data[0].split(',')]
    boards = []
    board = []
    for row in data[2:]:
        z = row.strip()
        if z:
            board.append(list(map(int, z.split())))
        else:
            boards.append(board)
            board = []
    if board:
        boards.append(board)

    for n in numbers:
        for i in range(len(boards)):
            for row in boards[i]:
                if n in row:
                    row[row.index(n)] = -1
                    break

        for b in boards:
            for row in b:
                if all(x == -1 for x in row):
                    return sum_board(b) * n
            bt = list(zip(*b))
            for row in bt:
                if all(x == -1 for x in row):
                    return sum_board(b) * n

def part_b(input):
    data = input.splitlines('\n\n')
    numbers = [int(x) for x in data[0].split(',')]
    boards = []
    board = []
    for row in data[2:]:
        z = row.strip()
        if z:
            board.append(list(map(int, z.split())))
        else:
            boards.append(board)
            board = []
    if board:
        boards.append(board)

    won_boards = set()

    for n in numbers:
        for i in range(len(boards)):
            if i in won_boards:
                continue
            for row in boards[i]:
                if n in row:
                    row[row.index(n)] = -1
                    break

        # Check for winners
        for i, b in enumerate(boards):
            if i in won_boards:
                continue

            for row in b:
                if all(x == -1 for x in row):
                    won_boards.add(i)
                    if len(won_boards) == len(boards):
                        return sum_board(b) * n
            bt = list(zip(*b))
            for row in bt:
                if all(x == -1 for x in row):
                    won_boards.add(i)
                    if len(won_boards) == len(boards):
                        return sum_board(b) * n

