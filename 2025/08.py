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
    for (a, b), d in list(sorted_dists.items())[:1000]:
        island_a = None
        island_b = None
        for island in islands:
            if a in island:
                island_a = island
            if b in island:
                island_b = island

        if island_a is not None and island_b is not None:
            if island_a is island_b:
                continue
            else:
                island_a.update(island_b)
                islands.remove(island_b)
        elif island_a is not None:
            island_a.add(b)
        elif island_b is not None:
            island_b.add(a)
        else:
            islands.append(set([a, b]))

    sorted_islands = sorted(islands, key=lambda x: -len(x))
    return len(sorted_islands[0]) * len(sorted_islands[1]) * len(sorted_islands[2])

def part_b(input):
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
    for (a, b), d in list(sorted_dists.items()):
        island_a = None
        island_b = None
        for island in islands:
            if a in island:
                island_a = island
            if b in island:
                island_b = island

        if island_a is not None and island_b is not None:
            if island_a is island_b:
                continue
            else:
                island_a.update(island_b)
                islands.remove(island_b)
        elif island_a is not None:
            island_a.add(b)
        elif island_b is not None:
            island_b.add(a)
        else:
            islands.append(set([a, b]))

        if len(islands) == 1 and len(islands[0]) == num_points:
            pos_a, pos_b = arr[:, a], arr[:, b]
            return pos_a[0] * pos_b[0]
