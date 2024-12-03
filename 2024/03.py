import re

def qwer(txt):
    asdf = re.findall(r"\d+", txt)
    res = 1
    for x in asdf:
        res = res * int(x)
    return res

def part_a(input):
    res = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)
    for a,b in matches:
        res = res + int(a) * int(b)
    return res

def part_b(input):
    res = 0
    do_starts = []
    for match in re.finditer(r"do\(\)", input):
        do_starts.append(match.start())
    do_starts = sorted(do_starts)

    dont_starts = []
    for match in re.finditer(r"don't\(\)", input):
        dont_starts.append(match.start())
    dont_starts = sorted(dont_starts)

    for match in re.finditer(r"mul\((\d+),(\d+)\)", input):
        pos = match.start()
        # Figure out if this is a do or don't by finding the closest do or dont
        closest_do = -1
        closest_dont = -1

        if do_starts:
            for x in do_starts:
                if x < pos:
                    closest_do = x

        if dont_starts:
            for x in dont_starts:
                if x < pos:
                    closest_dont = x

        if closest_do < 0 and closest_dont < 0:
            res = res + qwer(match.group())
        elif closest_do < 0 and closest_dont >= 0:
            pass
        elif closest_do >= 0 and closest_dont < 0:
            res = res + qwer(match.group())
        else:
            if closest_do < closest_dont:
                pass
            else:
                res = res + qwer(match.group())
    return res
