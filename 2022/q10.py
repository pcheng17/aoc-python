from aocd import data




def parse(data):
    return data.splitlines()

def signalStrength(cycle, value):
    cycles = [20, 60, 100, 140, 180, 220]
    if cycle in cycles:
        return cycle * value
    else:
        return 0

def partA(instructions):
    value = 1
    cycle = 0
    strength = 0
    for line in instructions:
        _, *num = line.split()
        if len(num) > 0:
            # Start of cycle
            cycle +=1

            # During cycle
            strength += signalStrength(cycle, value)

            # End of cycle 

            # Start of cycle 
            cycle += 1

            # During cycle
            strength += signalStrength(cycle, value)

            # End of cycle
            value += int(num[0])
        else:
            # Start of cycle 
            cycle += 1

            # During cycle
            strength += signalStrength(cycle, value)

            # End of cycle

    return strength


def partB(instructions):
    pixels = ['.' for _ in range(240)]
    value = 1
    cycle = 0
    for line in instructions:
        _, *num = line.split()
        if len(num) > 0:
            # Start of cycle
            cycle += 1
    
            # During cycle
            if abs(((cycle-1) % 40) - value) <= 1:
                pixels[cycle-1] = '#'

            # End of cycle

            # Start of cycle
            cycle += 1

            # During cycle
            if abs(((cycle-1) % 40) - value) <= 1:
                pixels[cycle-1] = '#'

            # End of cycle
            value += int(num[0])
        else:
            # Start of cycle
            cycle += 1

            # During cycle
            if abs(((cycle-1) % 40) - value) <= 1:
                pixels[cycle-1] = '#'

            # End of cycle
    
    return pixels


instructions = parse(data)
print(f'Part A: {partA(instructions)}')

print(f'Part B:')
resultStr = ''.join(partB(instructions))
resultOutput = '\n'.join([resultStr[i:i+40] for i in range(0, 240, 40)])
print(resultOutput)



