def blink(stone):
    out = []
    if stone == 0:
        out.append(1)
    elif len(str(stone)) % 2 == 0:
        numStr = str(stone)
        N = len(numStr)
        out.append(int(numStr[:N//2]))
        out.append(int(numStr[N//2:]))
    else:
        out.append(stone * 2024)
    return out

def solve(input, blinks):
    collection = {int(x) : 1 for x in input.split(" ")}
    for _ in range(blinks):
        newColllection = {}
        for stone, count in collection.items():
            for newStone in blink(stone):
                if newStone in newColllection:
                    newColllection[newStone] += count
                else:
                    newColllection[newStone] = count
        collection = newColllection
    return sum(collection.values())

def part_a(input):
    return solve(input, 25)

def part_b(input):
    return solve(input, 75)


