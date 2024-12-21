import itertools
import re

def get_keypresses(start, end, to_coord):
    di, dj = end[0] - start[0], end[1] - start[1]
    path = []
    if dj >= 0:
        path += [">"] * dj
        if di >= 0:
            path += ["v"] * di
        else:
            path += ["^"] * -di
    else:
        if di >= 0:
            path += ["v"] * di
        else:
            path += ["^"] * -di
        path += ["<"] * -dj
    return ''.join(path)

    # # minimize travel distance
    # tdmin = float("inf")
    # for p in itertools.permutations(path):
    #     tmp = ["A"] + list(p) + ["A"]
    #     coords = [to_coord[x] for x in tmp]
    #     if to_coord['X'] in coords:
    #         continue
    #     td = 0
    #     for i in range(len(coords)-1):
    #         a, b = coords[i], coords[i+1]
    #         td += abs(a[0] - b[0]) + abs(a[1] - b[1])
    #     if td < tdmin:
    #         tdmin = td
    #         path = p
    #
    # path = list(path) + ["A"]
    # return path

def process_path(path, start, coord_to_key):
    curr = start
    output = []
    for c in path:
        if c == "v":
            curr = (curr[0] + 1, curr[1])
        elif c == "^":
            curr = (curr[0] - 1, curr[1])
        elif c == ">":
            curr = (curr[0], curr[1] + 1)
        elif c == "<":
            curr = (curr[0], curr[1] - 1)
        output.append(coord_to_key[curr])
    return output

keypad_to_coord = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    'X': (3, 0),
    '0': (3, 1),
    'A': (3, 2),
}

coord_to_keypad = {v: k for k, v in keypad_to_coord.items()}

wasd_to_coord = {
    'X': (0, 0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2)
}

coord_to_wasd = {v: k for k, v in wasd_to_coord.items()}

def solve(code):
    tmp = f"A{code}"
    zxcv = []
    for c1, c2 in zip(tmp, tmp[1:]):
        kp = get_keypresses(keypad_to_coord[c1], keypad_to_coord[c2], wasd_to_coord)
        r2perms = set([''.join(x) for x in itertools.permutations(kp)])
        print(f"R2 :: {c1} -> {c2}: {r2perms}")
        best_asdf_length = float("inf")
        best_asdf = None
        for z in r2perms:
            print(f"  Working on {z}")

            if 'X' in process_path(z, keypad_to_coord[c1], coord_to_keypad):
                print(f"  Skipping {z}")
                continue

            tmp2 = "A" + z + "A"
            asdf = []
            for c3, c4 in zip(tmp2, tmp2[1:]):
                wp = get_keypresses(wasd_to_coord[c3], wasd_to_coord[c4], wasd_to_coord)
                r1perms = set([''.join(x) for x in itertools.permutations(wp)])
                print(f"  R1 :: {c3} -> {c4}: {r1perms}")
                best_qwer_length = float("inf")
                best_qwer = None
                for y in r1perms:
                    print(f"    Working on {y}")

                    if 'X' in process_path(y, wasd_to_coord[c3], coord_to_wasd):
                        print(f"    Skipping {y}")
                        continue

                    tmp3 = "A" + y + "A"
                    qwer = []
                    for c5, c6 in zip(tmp3, tmp3[1:]):
                        start, end = wasd_to_coord[c5], wasd_to_coord[c6]
                        mp = get_keypresses(start, end, wasd_to_coord)
                        qwer.append(mp)
                        print(f"    Me :: {c5} -> {c6}: {''.join(mp)}")
                    qwer = 'A'.join(qwer) + 'A'
                    print(f"    Me: {qwer}")

                    if len(qwer) < best_qwer_length:
                        best_qwer_length = len(qwer)
                        best_qwer = qwer

                print(f"  Best Me: {best_qwer}")
                asdf.append(best_qwer)
            asdf = 'A'.join(asdf) + 'A'
            print(f"  Asdf: {asdf}")

            if len(asdf) < best_asdf_length:
                best_asdf_length = len(asdf)
                best_asdf = asdf

        zxcv.append(best_asdf)
    zxcv = 'A'.join(zxcv) + 'A'
    return zxcv

def part_a(input):
    data = input.splitlines()
    for row in data[0:1]:
        print(f"Solving: {row}")
        ans = solve(row)
        print(f"Answer: {len(ans)}")







    #     print(f"Robot2: {''.join(robot2_path)}")
    #     z = process_path(robot2_path, keypad_to_coord['A'], coord_to_keypad)
    #     print(f"Sanity check: {''.join(z)}")
    #
    #     tmp = ["A"] + robot2_path
    #     robot1_path = []
    #     for i in range(len(tmp)-1):
    #         c1, c2 = tmp[i], tmp[i+1]
    #         start, end = wasd_to_coord[c1], wasd_to_coord[c2]
    #         robot1_path.extend(get_keypresses(start, end, wasd_to_coord))
    #
    #     print(f"Robot1: {''.join(robot1_path)}")
    #     z = process_path(robot1_path, wasd_to_coord['A'], coord_to_wasd)
    #     print(f"Sanity check: {''.join(z)}")
    #
    #     tmp = ["A"] + robot1_path
    #     me_path = []
    #     for i in range(len(tmp)-1):
    #         c1, c2 = tmp[i], tmp[i+1]
    #         start, end = wasd_to_coord[c1], wasd_to_coord[c2]
    #         me_path.extend(get_keypresses(start, end, wasd_to_coord))
    #
    #     print(f"Me: {''.join(me_path)}")
    #     z = process_path(me_path, wasd_to_coord['A'], coord_to_wasd)
    #     print(f"Sanity check: {''.join(z)}")
    #     print("\n")
    #
    #     me.append(''.join(me_path))
    #
    # solutions = [
    #     "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
    #     "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
    #     "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    #     "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
    #     "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    # ]
    #
    # s = solutions[-1]
    # print(f"==================================================")
    # print(f"Me     : {s}")
    # z = process_path(s, wasd_to_coord['A'], coord_to_wasd)
    # print(f"Robot 1: {''.join(z)}")
    # z = process_path(z, wasd_to_coord['A'], coord_to_wasd)
    # print(f"Robot 2: {''.join(z)}")
    # z = process_path(z, keypad_to_coord['A'], coord_to_keypad)
    # print(f"Robot 3: {''.join(z)}")
    #
    # s = me[-1]
    # print(f"==================================================")
    # print(f"Me     : {s}")
    # z = process_path(s, wasd_to_coord['A'], coord_to_wasd)
    # print(f"Robot 1: {''.join(z)}")
    # z = process_path(z, wasd_to_coord['A'], coord_to_wasd)
    # print(f"Robot 2: {''.join(z)}")
    # z = process_path(z, keypad_to_coord['A'], coord_to_keypad)
    # print(f"Robot 3: {''.join(z)}")
    #
    #
    #
    # total = 0
    # for row, path in zip(data, me):
    #     numcode = re.findall(r'\d+', row)
    #     total += int(numcode[0]) * len(path)
    # return total

def part_b(input):
    data = input.splitlines()
