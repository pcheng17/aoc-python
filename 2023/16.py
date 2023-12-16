def advance(n):
    if n[2] == '^':
        return (n[0]-1, n[1], '^')
    elif n[2] == '>':
        return (n[0], n[1]+1, '>')
    elif n[2] == 'V':
        return (n[0]+1, n[1], 'V')
    else:
        return (n[0], n[1]-1, '<')

def solve(data, start):
    rows = len(data)
    cols = len(data[0])

    frontier = [start]

    visited = set()
    visited.add(start)

    while frontier:
        next_frontier = []
        for i, j, d in frontier:
            if data[i][j] == '.':
                next_frontier.append(advance((i, j, d)))
            elif data[i][j] == '|':
                if d == '>' or d == '<':
                    next_frontier.append((i+1, j, 'V'))
                    next_frontier.append((i-1, j, '^'))
                elif d == 'V':
                    next_frontier.append((i+1, j, 'V'))
                else:
                    next_frontier.append((i-1, j, '^'))
            elif data[i][j] == '-':
                if d == 'V' or d == '^':
                    next_frontier.append((i, j+1, '>'))
                    next_frontier.append((i, j-1, '<'))
                elif d == '>':
                    next_frontier.append((i, j+1, '>'))
                else:
                    next_frontier.append((i, j-1, '<'))
            elif data[i][j] == '\\':
                if d == '>':
                    next_frontier.append((i+1, j, 'V'))
                elif d == 'V':
                    next_frontier.append((i, j+1, '>'))
                elif d == '<':
                    next_frontier.append((i-1, j, '^'))
                else:
                    next_frontier.append((i, j-1, '<'))
            else:
                if d == '>':
                    next_frontier.append((i-1, j, '^'))
                elif d == 'V':
                    next_frontier.append((i, j-1, '<'))
                elif d == '<':
                    next_frontier.append((i+1, j, 'V'))
                else:
                    next_frontier.append((i, j+1, '>'))
        
        # Filter
        next_frontier = [n for n in next_frontier if 0 <= n[0] < rows]
        next_frontier = [n for n in next_frontier if 0 <= n[1] < cols]
        next_frontier = [n for n in next_frontier if n not in visited]
        for n in next_frontier:
            visited.add(n)
        frontier = next_frontier 
        if not frontier:
            break
    
    # Filter visited
    visited = set((n[0], n[1]) for n in visited)
    return len(visited)

def part_a(input):
    data = input.splitlines()
    return solve(data, (0, 0, '>'))

def part_b(input):
    data = input.splitlines()

    rows = len(data)
    cols = len(data[0])

    top = max(solve(data, (0, j, 'V')) for j in range(cols))
    bottom = max(solve(data, (rows-1, j, '^')) for j in range(cols))

    left = max(solve(data, (i, 0, '>')) for i in range(rows))
    right = max(solve(data, (i, cols-1, '<')) for i in range(rows))

    return max(top, bottom, left, right)


