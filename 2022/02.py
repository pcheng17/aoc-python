shape = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

losesAgainst = {
    'A': 3,
    'B': 1,
    'C': 2
}

winsAgainst = {
    'A': 2,
    'B': 3,
    'C': 1
}

tiesAgainst = {
    'A': 1,
    'B': 2,
    'C': 3
}

LOST = 0;
DRAW = 3;
WON = 6;

def rps(theirs, yours):
    if theirs == 'A':
        if yours == 'X': return DRAW
        elif yours == 'Y': return WON
        else: return LOST
    elif theirs == 'B':
        if yours == 'X': return LOST
        elif yours == 'Y': return DRAW
        else: return WON
    else:
        if yours == 'X': return WON
        elif yours == 'Y': return LOST
        else: return DRAW

def solve_b(theirs, outcome):
    if outcome == 'X': return losesAgainst[theirs] + LOST
    elif outcome == 'Y': return tiesAgainst[theirs] + DRAW
    else: return winsAgainst[theirs] + WON

def part_a(input):
    total = 0
    for game in input.splitlines():
        theirs, yours = game.split(' ');
        total += rps(theirs, yours) + shape[yours]
    return total

def part_b(input):
    total = 0
    for game in input.splitlines():
        theirs, outcome = game.split(' ');
        total += solve_b(theirs, outcome)
    return total
