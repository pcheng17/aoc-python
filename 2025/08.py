from collections import OrderedDict
import numpy as np

def part_a(input):
    data = input.splitlines()
    num_points = len(data)
    data_flat = []
    for row in data:
        data_flat.extend(list(map(int, row.split(','))))
    arr = np.array(data_flat).reshape((3, num_points), order='F')

    dists = {}
    for i in range(num_points):
        for j in range(i + 1, num_points):
            d = np.sum((arr[:, i] - arr[:, j]) ** 2) ** 0.5
            dists[(i, j)] = d

    sorted_dists = OrderedDict(sorted(dists.items(), key=lambda x: x[1]))
    islands = []
    connections = 0
    for (a, b), d in list(sorted_dists.items()):
        print(f"Processing pair: ({a}, {b}) (distance = {d})")
        island_a = None
        island_b = None
        for island in islands:
            if a in island:
                island_a = island
            if b in island:
                island_b = island

        if island_a is not None and island_b is not None:
            if island_a is island_b:
                print(f"  Both points already in the same island: {island_a}")
                continue
            else:
                print(f"  Connecting islands: {island_a} and {island_b}")
                island_a.update(island_b)
                islands.remove(island_b)
                connections += 1
        elif island_a is not None:
            print(f"  Adding {b} to island {island_a}")
            island_a.add(b)
            connections += 1
        elif island_b is not None:
            print(f"  Adding {a} to island {island_b}")
            island_b.add(a)
            connections += 1
        else:
            print(f"  Creating new island with {a} and {b}")
            islands.append(set([a, b]))
            connections += 1

        print(f"  Current islands: {islands}")
        print(f"  Total connections made: {connections}")
        if connections == 10:
            break

    print(islands)
    sorted_islands = sorted(islands, key=lambda x: -len(x))
    print(sorted_islands)
    return len(sorted_islands[0]) * len(sorted_islands[1]) * len(sorted_islands[2])

def part_b(input):
    data = input.splitlines()
